# User accounts and logins

class users:
    name = ''
    pw = ''
    IsT = False
    stake = [10] # a default stake. Has stake for every subjects. 각 분야(리스트)마다 지분이 존재함
    vrs = [] # verification records. 사용자 인증 기록
epws = [] # pw encrypted text of name. contains all users' epw.

def createacc():
    #
    print('something')
