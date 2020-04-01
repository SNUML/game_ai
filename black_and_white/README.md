# game_ai
[SNUML] Black and White Game API

실행 방법
------------------

    python run.py -f FILE1 FILE2 -c COUNT

로 실행 가능합니다. 실행 시 FILE1과 FILE2에 구현된 전략이 각각 player 1, 2가 되어 총 COUNT번 대결합니다.
FILE1, FILE2는 "알고리즘 구현" 조건을 만족하는 파이썬 파일의 경로여야 합니다.
문제 없이 실행되었다면 player 1과 player 2의 승리 횟수를 출력하고 종료합니다.

각 인자별 구체적인 설명은

    python run.py --help

로 확인 가능합니다.


알고리즘 구현
-------------------

FILE1, FILE2에는 query 메소드를 포함하는 Player클래스가 정의돼 있어야 합니다.

query 메소드는 각 게임에서 라운드마다 한 번씩 호출됩니다.
frame.py에 정의된 PlayerVisibleState의 인스턴스인 state를 인자로 받고, 이번 라운드에서 뽑은 타일에 적힌 숫자를 반환해야 합니다. 

자세한 구현은 models/template.py를 참조하세요.