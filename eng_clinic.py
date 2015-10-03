# Automatic reservation for KAIST english clinic
# Developed by YP KOO 2015

import requests

LOGIN_URL = 'http://hss.kaist.ac.kr/sub06/proin_proc.php'
RESERVE_URL = 'http://hss.kaist.ac.kr/sub11/01_01_01_pro.php'

login_payload = {
    'user_id': '',
    'user_pwd': ''
}

with requests.Session() as s:
    # Authentication
    p = s.post(LOGIN_URL, data=login_payload)
    print p.text

    p = s.get('http://hss.kaist.ac.kr/sub11/01_01_01.php?search_term_idx=7&search_room=1')
    print p.text

    reserve_payload = {
        'search_term_idx': '',
        'search_room': '',
        'weeks': '',
        'clendar_ym': '',
        'clendar_ymd': '',
        'faculty': '',
        'faculty_idx': '',
        'reserv_date': '',
        'reserv_stime': '',
        'reserv_etime': '',
        'student_name': '',
        'student_id': '',
        'student_email': '',
        'student_phone': '',
        'student_year': '',
        'clinic_gbn': '',
        'portal_id': '',
        'cancel_yn': '',
        'attend_yn': '',
    }
