"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000  # chi phí cố định 40 triệu đ/tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1.0 / p if k is None else (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL, luong_phut=LUONG_PHUT,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])].copy()
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000.0 * gia_vao + runs['tokens_out'] / 1000.0 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = float(reqs['phut_xem_lai_simulated'].sum()) * luong_phut * he_so_xem_lai
    lam_lai = float(reqs['phut_lam_lai_simulated'].sum()) * luong_phut * he_so_lam_lai
    tong = float(tien_token.sum() + tien_tool.sum()) + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    khong_thanh_cong = int(len(reqs) - thanh_cong)
    chay_lai = float((tien_token + tien_tool)[runs['attempt'] > 1].sum())

    return {
        'token': float(tien_token.sum()),
        'tool': float(tien_tool.sum()),
        'chay_lai': chay_lai,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'khong_thanh_cong': khong_thanh_cong,
        'cps': tong / thanh_cong,
        'hoa_don_moi_yc': float(tien_token.sum() + tien_tool.sum()) / len(reqs),
    }


def in_nhiem_vu_a3_a4(runs, reqs):
    """Nhiệm vụ A3 (tách theo loại) và A4 (chi phí cố định cho phạm vi noi_dia + hang_nang)."""
    print('\n---------- Nhiệm vụ A3 · Tách theo loại yêu cầu ----------')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        tl_tc = kq['thanh_cong'] / len(sub) * 100
        lan_tb = sub['so_lan_chay'].mean()
        print(
            f"{loai:10s} | yc={len(sub):3d} | tc={tl_tc:5.1f}% | "
            f"lan/yc={lan_tb:4.2f} | cps(sim)={kq['cps']:8,.0f} đ | "
            f"so_12k={kq['cps'] / BASELINE:4.2f}x"
        )

    merged = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    merged['ok'] = (merged['status'] == 'ok').astype(int)
    bang_ok = merged.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean') * 100
    print('\nTỉ lệ status == ok theo lần chạy (%):')
    print(bang_ok.round(1).to_string())

    print('\n---------- Nhiệm vụ A4 · Chi phí cố định (noi_dia + hang_nang) ----------')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, pv)
    for nhan, khoi_luong in [('45.000 yc/thang', 45_000), ('22.500 yc/thang (1/2)', 22_500)]:
        tc_thang = khoi_luong * (kq_pv['thanh_cong'] / len(reqs))
        cd_moi_viec = CO_DINH_THANG / tc_thang
        tong_moi_viec = kq_pv['cps'] + cd_moi_viec
        print(
            f"{nhan:22s} | tc/thang={tc_thang:8,.0f} | co_dinh={cd_moi_viec:6,.0f} đ | "
            f"cps+cd(sim)={tong_moi_viec:6,.0f} đ ({tong_moi_viec / BASELINE:4.2f}x)"
        )


def in_nhiem_vu_b(runs, reqs):
    """Nhiệm vụ B1–B4: độ nhạy, đổi cặp, giới hạn chạy lại và xem lại 100%."""
    print('\n---------- Nhiệm vụ B1 · Bảng độ nhạy ----------')
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Tỉ lệ xem lại gấp đôi': dict(he_so_xem_lai=2.0),
        'Tỉ lệ xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Số ca làm lại gấp đôi': dict(he_so_lam_lai=2.0),
        'Số ca làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương nhân viên tăng 25%': dict(luong_phut=2500),
        'Chỉ cho chạy tối đa 2 lần': dict(max_lan_chay=2),
        'Chỉ cho chạy 1 lần': dict(max_lan_chay=1),
    }
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f"{ten:28s} | cps(sim)={cps:8,.0f} đ | {(cps / goc - 1) * 100:+6.1f}%")

    print('\n---------- Nhiệm vụ B2 · Đổi một cặp ----------')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)['cps']
    print(f"Token x2 + Xem lại x2        | cps(sim)={cps_cap:8,.0f} đ | {(cps_cap / goc - 1) * 100:+6.1f}%")

    print('\n---------- Nhiệm vụ B3 · Chi phí cả hệ thống theo giới hạn chạy ----------')
    for k in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=k)
        ca_ht = kq_k['tong'] + kq_k['khong_thanh_cong'] * BASELINE
        print(
            f"Gioi han {k} lan | tong_tro_ly(sim)={kq_k['tong']:10,.0f} đ | "
            f"khong_tc={kq_k['khong_thanh_cong']:3d} | ca_he_thong(sim)={ca_ht:10,.0f} đ | "
            f"cps(sim)={kq_k['cps']:6,.0f} đ"
        )

    print('\n---------- Nhiệm vụ B4 · Xem lại 100% (noi_dia + hang_nang) ----------')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    co_ok = runs_pv.groupby('request_id')['status'].apply(lambda s: (s == 'ok').any()).sum()
    so_lam_lai = int((pv['ket_qua'] == 'lam_lai').sum())
    tc_pv = int((pv['ket_qua'] == 'thanh_cong').sum())
    tien_trace_pv = (
        (runs_pv['tokens_in'] / 1000.0 * GIA_VAO + runs_pv['tokens_out'] / 1000.0 * GIA_RA).sum()
        + (runs_pv['tool_calls'] * GIA_TOOL).sum()
    )
    tb_lam_lai_toan_bo = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    tv_lam_lai_toan_bo = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].median()
    print(f"So yc co it nhat 1 run ok={co_ok}, so ca lam_lai={so_lam_lai}, thanh_cong={tc_pv}, trace={tien_trace_pv:,.0f} đ")
    print(f"phut_lam_lai_simulated (toan bo ca lam_lai): mean={tb_lam_lai_toan_bo:.2f}, median={tv_lam_lai_toan_bo:.2f}")
    for nhan, phut_ll in [('Gia dinh 9 phut/ca', 9.0), (f'Thuc te {tb_lam_lai_toan_bo:.2f} phut/ca', tb_lam_lai_toan_bo)]:
        xem_100 = co_ok * 5.0 * LUONG_PHUT
        lam_lai_cost = so_lam_lai * phut_ll * LUONG_PHUT
        tong_b4 = tien_trace_pv + xem_100 + lam_lai_cost
        cps_b4 = tong_b4 / tc_pv
        hoa_von = (BASELINE * tc_pv - tien_trace_pv - lam_lai_cost) / (co_ok * LUONG_PHUT)
        print(
            f"  {nhan:26s} | tong(sim)={tong_b4:10,.0f} đ | cps(sim)={cps_b4:7,.0f} đ "
            f"({cps_b4 / BASELINE:4.2f}x) | hoa von xem lai <= {hoa_von:.2f} phut"
        )


def co_mau_cong_thuc(p1, p2, alpha=0.05, power=0.80):
    """Công thức cỡ mẫu mỗi nhóm khi so hai tỉ lệ."""
    za = NormalDist().inv_cdf(1.0 - alpha / 2.0)
    zb = NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2.0
    return math.ceil(
        (za * math.sqrt(2.0 * pb * (1.0 - pb)) + zb * math.sqrt(p1 * (1.0 - p1) + p2 * (1.0 - p2))) ** 2
        / (p2 - p1) ** 2
    )


def in_nhiem_vu_d1(reqs):
    """Nhiệm vụ D1 · Tính cỡ mẫu 5 câu và tỉ lệ mở lại hiện tại cho pilot_plan.yaml."""
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower

    print('\n---------- Nhiệm vụ D1 · Cỡ mẫu pilot (baseline=0.70, alpha=0.05, power=0.80, ICC=0.02) ----------')
    p1, p2_5pt, p2_6pt = 0.70, 0.75, 0.76
    alpha, power, icc = 0.05, 0.80, 0.02

    n_5pt_ct = co_mau_cong_thuc(p1, p2_5pt, alpha, power)
    n_5pt_sm = math.ceil(NormalIndPower().solve_power(proportion_effectsize(p1, p2_5pt), power=power, alpha=alpha))
    de_75 = 1.0 + (75 - 1) * icc
    n_nhan_vien_75 = math.ceil(n_5pt_ct * de_75)
    so_nv_moi_nhom = math.ceil(n_nhan_vien_75 / 75)
    gioi_han_20_nv = 20 / icc
    gioi_han_6_depot = 6 / icc

    n_6pt_ct = co_mau_cong_thuc(p1, p2_6pt, alpha, power)
    m_min_6pt = math.ceil(n_6pt_ct * (1.0 - icc) / (20.0 - n_6pt_ct * icc))
    de_6pt = 1.0 + (m_min_6pt - 1) * icc
    power_neu_5pt = NormalIndPower().power(
        proportion_effectsize(p1, p2_5pt), nobs1=n_6pt_ct, alpha=alpha, ratio=1.0
    )

    print(f"a) Chia theo yeu cau (5 diem): cong thuc={n_5pt_ct:,} yc/nhom (statsmodels={n_5pt_sm:,})")
    print(f"b) Theo nhan vien (m=75): DE={de_75:.2f} -> can {n_nhan_vien_75:,} yc/nhom ({so_nv_moi_nhom} nguoi/nhom, tong {so_nv_moi_nhom * 2} > 40)")
    print(f"c) 20 nhan vien/nhom: gioi han c/ICC = {gioi_han_20_nv:,.0f} < {n_5pt_ct:,} -> KHONG DAT")
    print(f"d) 6 depot/nhom: gioi han c/ICC = {gioi_han_6_depot:,.0f} < {n_5pt_ct:,} -> KHONG DAT")
    print(f"e) Muc chenh 6 diem: can {n_6pt_ct:,} yc hieu dung/nhom; voi 20 nv/nhom -> m >= {m_min_6pt} yc/nguoi (DE={de_6pt:.2f})")
    print(f"   Luu y bat loi: neu tac dong that la 5 diem voi n_eff={n_6pt_ct}, power con {power_neu_5pt:.2f}")

    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    print(
        f"Ti le mo_lai_trong_7_ngay hien tai: toan mau={reqs['mo_lai_trong_7_ngay'].mean() * 100:.2f}% "
        f"({int(reqs['mo_lai_trong_7_ngay'].sum())}/{len(reqs)}), "
        f"pham vi noi_dia+hang_nang={pv['mo_lai_trong_7_ngay'].mean() * 100:.2f}% "
        f"({int(pv['mo_lai_trong_7_ngay'].sum())}/{len(pv)})"
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)

    kiem_tra_dap_an_biet_truoc()

    print('\n---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.0f}')
    print(f"Gap hoa don/yc   {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:>14.1f}x")
    ca_ht_a2 = (ket_qua['tong'] + ket_qua['khong_thanh_cong'] * BASELINE) / len(reqs)
    print(f"Ca he thong/yc   {ca_ht_a2:>14,.0f} đ ({ca_ht_a2 / BASELINE:.2f}x của 12.000 đ) [simulated]")

    in_nhiem_vu_a3_a4(runs, reqs)
    in_nhiem_vu_b(runs, reqs)
    in_nhiem_vu_d1(reqs)
