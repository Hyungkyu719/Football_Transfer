# Football_Transfer
DB project

-------
1st commit 11/30

DB 작성 및 병합

League(EPL,Bundesliga,LaLiga,SerieA,Ligue1) - 직접작성

Transfer - Football transfers 2007 - 2017(https://www.kaggle.com/vardan95ghazaryan/transfers-in-1617-season)

Fulldata - Complete FIFA 2017 Player dataset (Global)(https://www.kaggle.com/artimous/complete-fifa-2017-player-dataset-global?select=FullData.csv)


2nd commit 12/1

DB 일부 수정(필요없는 정보 삭제 및 table간 Club명 일치 작업)


3rd commit 12/4

DB 2차 일부 수정(table간 Club명 일치 작업)

4th commit 12/11

DB 3차 일부 수정(table간 선수명, club명 일치 작업 마무리 및 선수명,club명에 들어간 특수문자 제거)

football_transfer_project.py 작성 

-Selet a League -League(Bundesliga,EPL ..)클릭 후 url창에 마지막에 /등수 추가하면 해당 구단의 선수정보 확인

ex)http://127.0.0.1:5000/football_transfer/select_league/bundesliga/1 -> FC Bayern의 선수정보 출력

5th commit 12/14

DB 4차 일부 수정(League table 생성하여 기존의 EPL,Bundesliga,LaLiga,SerieA,Ligue1 병합)

url에 직접 타이핑하여 선수정보 확인하는거에서 팀명으로 검색하도록 변경

Transfer data또한 선수명, 팀명으로 검색하는 기능 추가
