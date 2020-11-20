# AIGARET

AIGARET(AI Game Rehabilitation Trainer)은 신체 움직임을 통해 조작할 수 있는 게임으로 집에서 가볍게 즐길 수 있는 재활 트레이닝 프로그램입니다.

## 프로젝트 기획 배경

> 최근 코로나로 인해서 사회 전반에 걸쳐 사람간의 접촉을 최소화하는 언택트 사회로 전환하고자 하는 움직임이 일고있습니다. 하지만 소수에 해당하는 장애인들을 위한 방안은 상대적으로 적은 것이 사실입니다. 그 중에서도 재활을 위해 주기적으로 병원에 방문해야 하는 장애인들의 경우 코로나로 인한 재활병원의 외래 기능 중단, 축소와 함께 코로나 감염 우려로 외출 빈도가 감소하게 되면서 재활에 큰 타격을 받고있습니다.[1] 신체기능의 상실을 겪은 장애인들의 경우 꾸준한 재활 훈련을 통해 잔존기능을 유지하고 회복하는 것에 초점을 맞춘다면 일반인들과 마찬가지로 충분히 직업생활을 영위하는 것이 가능합니다. 또한 재활의 마지막 단계로써 직장생활과 같은 일상생활을 영위하게 되더라도 재활 훈련을 지속적으로 진행하는 것이 중요합니다.[2] 하지만 현재와 같이 코로나 사태가 지속되어 장애인들의 재활이 오랜기간 중단된다면, 잔존기능의 저하가 발생하게 되어 장애인들의 직업생활에도 부정적인 영향을 미칠 수 있습니다. 이런 문제점을 해결하기 위해 병원에 가지 않고도 집에서 가벼운 신체운동을 동반한 게임을 통해 잔존기능의 상실을 최소화 할 수 있는 AI 게임 재활 트레이너를 구상하였습니다.

- [1] [재활-수업 ‘산넘어 산’… 코로나에 더 힘겨운 장애인](https://www.donga.com/news/Society/article/all/20200420/100721064/1)
- [2] [뇌졸중 환자 가족의 퇴원 후 교육요구도](https://ir.ymlib.yonsei.ac.kr/bitstream/22282913/122642/1/T008833.pdf) -keyword: 직장
- [Effects of aerobic training on physical activity in people with stroke: A randomized controlled trial](https://pubmed.ncbi.nlm.nih.gov/32250336/)
- [Game analysis and clinical use of the Xbox-Kinect for stroke rehabilitation](https://pubmed.ncbi.nlm.nih.gov/29994922/)
- [마비쪽 팔의 플레이싱 훈련이 뇌졸중 환자의 팔 뻗기 동작에 미치는 효과](http://jksnt.org/submission/proof/PDFMerger/savepdfs/111405_journal_1_201905191336.pdf)



## 서비스 개요

> AIGARET은 체간 안정화 훈련, 체중 중심 이동 훈련, 기능적 팔뻗기 훈련 등 실제 임상에서 적용되는 재활 훈련과 유사한 게임을 통해 집에서도 즐겁고 간편하게 사용할 수 있는 게임 재활 트레이닝 프로그램을 제공하는 서비스입니다. AIGARET에서 제공하는 게임은 화면 내의 열매 획득하기, 몸을 기울여 자동차 운전하기 등 웹캠을 통해 사용자의 신체 움직임을 파악하고 이를 통해 게임 내의 가상 객체를 조작하여 점수를 획득하는 방식으로 구성됩니다. 짧은 수행시간 또는 어려운 난이도의 작업을 수행할수록 더 높은 점수를 획득하여 사용자에게 동기부여가 가능합니다. 사용자는 질병과 기능 수준에 맞는 게임을 선택하여 진행 할 수 있고, 각 게임을 통해 획득한 점수는 사용자 정보에 저장되어 수행능력의 지속적인 추적 및 객관화가 가능합니다. 또한, 게임을 조합하여 훈련을 계획하고 실제로 훈련을 진행한 성취도를 평가하는 스케쥴링기능도 제공할 예정입니다.



## 설치 및 실행 방법

```
git clone https://lab.ssafy.com/s03-ai-sub2/s03p22b203.git
```

```
cd front-end
```

```
npm install
```

```
npm run serve
```



## 로그인 화면

```
http://localhost:8080/login
```

- 회원가입시 카메라 아이콘 버튼을 클릭해 얼굴을 인식해 DB에 저장할 예정입니다.



## 게임 화면

```
http://localhost:8080/game
```

  ### 1. 쥐를 잡자

 ![wristtouchgame](/uploads/0acdd154ef30cc0919fe9743ece7307a/wristtouchgame.png)
  
  #### :clipboard: 게임 설명
  플레이어는 고양이가 되어 화면 상에 무작위로 등장하는 생쥐를 잡아야합니다. 점점 더 빨리 도망치는 생쥐를 잡아 최고점수에 도전해 보세요!
  
  #### :warning: 주의사항
  컴퓨터 화면으로부터 최소 2미터 이상의 간격을 유지하고 자리에서 일어나서 플레이하는 것을 권장합니다.
  
  #### :hospital: 재활 효과
  - 상지의 불규칙적인 움직임을 지속적으로 유도하여 수술 및 질환으로 인해 감소한 ROM(Range of Motion)과 근지구력의 정상범위 회복을 기대할 수 있습니다.
  - 신체의 움직임을 화면 상에서 실시간으로 확인하여 고유수용성 감각에 대한 시각적 되먹임 훈련효과를 기대할 수 있습니다.
  - 생쥐와 손목부위의 지속적인 추적을 통해 인지 기능의 향상을 기대할 수 있습니다.
  
  #### :relaxed: 적응증
 - 근골격계 질환: 회전근개 파열, 골절, 유착성 관절낭염(오십견), 어깨관절 탈구 등 근골격계 질환으로 상지 ROM 및 근지구력에 저하를 겪은 환자
 - 신경계 질환: 뇌졸중, 파킨슨병, 진행성 근이영양증, 치매, 뇌성마비, 발달장애, 외상 및 질환으로 인한 신경 손상 등 뇌신경계질환으로 상지 ROM, 근지구력 및 인지능력에 저하를 겪은 환자

#### :video_game: 게임 실행 화면
![wristgameplay](/uploads/892c45c4eca348726f878d55b383fcdc/wristgameplay.png)
  
  
  ### 2. 스네이크 게임

![snakegame](/uploads/3eada5cd2e752783e9bf3d07ca07a65a/snakegame.png)
  
  #### :clipboard: 게임 설명
 플레이어는  배고픈 뱀을 위해 화면 상에 무작위로 등장하는 먹이를 먹을 수 있도록 도와줘야합니다. 배고픈 뱀이 점점 더 빨리 사라지는 먹이를 놓치지 않고 무사히 먹을 수 있도록 도와주세요!
  
  #### :warning: 주의사항
 컴퓨터 화면으로부터 최소 50센치 이상의 간격을 유지하고 자리에서 앉아서 플레이하는 것을 권장합니다.
  
  #### :hospital: 재활 효과
 - 몸통 및 머리의 굽힘, 폄 동작과 좌우 기울임 동작을 유도하여 수술 및 질환으로 인해 감소한 근지구력의 정상범위 회복과 스트레칭 효과를 기대할 수 있습니다.
  - 불규칙적인 기울임 동작을 유도함으로써 앉은 자세(혹은 선 자세)의 Static, Dynamic balance 향상을 기대할 수 있습니다.
 - 뱀과 먹이의 지속적인 추적을 통해 인지 기능의 향상을 기대할 수 있습니다.

  
  #### :relaxed: 적응증
 - 근골격계 질환: 경추, 흉추, 요추의 추간판 탈출증, LBP등 근골격계 질환으로 몸통 및 머리의 움직임 기능이 저하된 환자
 - 신경계 질환: 뇌졸중, 파킨슨병, 진행성 근이영양증, 치매, 뇌성마비, 발달장애, 외상 및 질환으로 인한 신경 손상 등 뇌신경계질환으로 몸통 및 머리의 Stability, Balance, 근지구력 및 인지능력에 저하를 겪은 환자

#### :video_game: 게임 실행 화면
![스네이크게임](/uploads/d0af576edc0ea6260827d38e8db05a6c/스네이크게임.png)


  ### 3. 환상의 점프

![jumpgame](/uploads/b50ce89fe21c69b6ae1ad576546c96ab/jumpgame.png)
  
  #### :clipboard: 게임 설명
 플레이어는  갈길이 바쁜 여우를 위해 화면 상에 무작위로 등장하는 장애물을 피할 수 있도록 도와줘야합니다. 점점 더 빨리 달리는 여우가 넘어지지 않도록 도와주세요!
  #### :warning: 주의사항
 컴퓨터 화면으로부터 최소 50센치 이상의 간격을 유지하여 플레이하는 것을 권장합니다.

 이 게임은 여우가 점프를 하도록 하는 자세와 달릴 수 있도록 하는 자세를 정해야합니다. 각 행동에 맞는 버튼을 누르고 빨간 글씨가 사라질때까지 자세를 충분히 유지해 주세요. 설정을 완료한 이후 학습하기 버튼을 누르고 빨간 글씨가 사라질때까지 잠시만 기다려주세요.학습이 완료된 이후 게임시작버튼을 눌러 플레이 하면 됩니다.

  
  #### :hospital: 재활 효과
 - 환자의 상태에 맞춰 원하는 부위의 훈련을 스스로 실행할 수 있습니다.
 - 여우와과 장애물의 지속적인 추적과 회피 훈련을 통해 인지 기능의 향상 및 순발력 향상을 기대할 수 있습니다.


  
  #### :relaxed: 적응증
 전문가의 조언에 맞게 훈련 상황을 셋팅하여 다양한 질환에 적용이 가능합니다.

#### :video_game: 게임 실행 화면
![점프게임](/uploads/fb5b043e6303c552624149ace229d247/점프게임.png)

