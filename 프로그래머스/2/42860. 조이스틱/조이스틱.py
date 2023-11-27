def solution(name):
    
    spell_move = 0
    
    # 커서 이동 횟수, 이름의 길이 - 1( 좌우 이동 )
    cursor_move = len(name) - 1  
    
    
    for i, spell in enumerate(name):
    	# 알파벳 변경 횟수, 위아래 중 최소 이동 값 ( 상하 이동 )
        spell_move += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 아래 3가지 경우 중 최소 이동 값으로 갱신
        # 1. 이전 커서 이동 값 ( 초기값 - 이름의 길이 - 1 )
        # 2. 연속된 A의 왼쪽 시작
        # 3. 연속된 A의 오른쪽 시작
        cursor_move = min([ cursor_move, 2 * i + len(name) - next, i + 2 * (len(name) - next) ])
        
        
    # 조이스틱 조작 횟수 = 알파벳 변경 횟수( 상하 이동 ) + 커서 이동 횟수( 좌우 이동 )    
    return spell_move + cursor_move
