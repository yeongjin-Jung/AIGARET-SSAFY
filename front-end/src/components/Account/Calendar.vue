<template>
  <v-container>
    <div id="calendar">
    </div>

    <div id="my_modal" style="width: 500px">
      <div id="modal_content">
      </div>
      <v-btn class="modal_close_btn" color="error">닫기</v-btn>
    </div>
  </v-container>
</template>

<script>
import $ from 'jquery'
import { mapActions } from 'vuex';

export default {
  name: "Calendar",
  data() {
    return {
      gameRecords: this.$store.state.gameRecords
    }
  },

  mounted() {
    const today = new Date();
    let y = today.getFullYear()
    let m = today.getMonth() + 1
    let d = today.getDate()

    // this.getRecords(y + "-" + (m >= 10 ? m : '0' + m) + "-" + (d >= 10 ? d : '0' + d))

    const setCalendarData = (year, month) => {
      let calHtml = "";

      const setDate = new Date(year, month - 1, 1);
      const firstDay = setDate.getDate();
      const firstDayName = setDate.getDay();
      const lastDay = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();
      const prevLastDay = new Date(today.getFullYear(), today.getMonth(), 0).getDate();

      let startDayCount = 1;
      let lastDayCount = 1;

      const todayMonth = today.getMonth();
      const todayDate = today.getDate();

      const stamp = '/img/stamp.833cb0bc.png'

      calHtml += `<div style='background-color: #e6e6e6; margin-bottom: 0.5%' class='calendar__day horizontalGutter'><span>일</span></div>`;
      calHtml += `<div style='background-color: #e6e6e6; margin-bottom: 0.5%' class='calendar__day horizontalGutter'><span>월</span></div>`;
      calHtml += `<div style='background-color: #e6e6e6; margin-bottom: 0.5%' class='calendar__day horizontalGutter'><span>화</span></div>`;
      calHtml += `<div style='background-color: #e6e6e6; margin-bottom: 0.5%' class='calendar__day horizontalGutter'><span>수</span></div>`;
      calHtml += `<div style='background-color: #e6e6e6; margin-bottom: 0.5%' class='calendar__day horizontalGutter'><span>목</span></div>`;
      calHtml += `<div style='background-color: #e6e6e6; margin-bottom: 0.5%' class='calendar__day horizontalGutter'><span>금</span></div>`;
      calHtml += `<div style='background-color: #e6e6e6; margin-bottom: 0.5%' class='calendar__day verticalGutter'><span>토</span></div>`;

      for (let i = 0; i < 6; i++) {
        for (let j = 0; j < 7; j++) {
          
          // 달력상 저번달 일자 표시
          if (i == 0 && j < firstDayName) {
            if (j == 0) {
              calHtml += `<div style='background-color: #FFFFBB;' class='calendar__day horizontalGutter'>
                            <p style="margin-bottom: 0; padding-bottom: 0">${ prevLastDay - (firstDayName - 1) + j }</p>
                            <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                          </div>`;
            } else if (j == 6) {
              calHtml += `<div style='background-color: #FFFFBB;' class='calendar__day'>
                            <p style="margin-bottom: 0; padding-bottom: 0">${ prevLastDay - (firstDayName - 1) + j }</p>
                            <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                          </div>`;
            } else {
              calHtml += `<div style='background-color: #FFFFBB;' class='calendar__day horizontalGutter'>
                            <p style="margin-bottom: 0; padding-bottom: 0">${ prevLastDay - (firstDayName - 1) + j }</p>
                            <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                          </div>`;
            }
          }
          
          // 이번달 시작 & 첫 주 && 1일
          else if (i == 0 && j == firstDayName) {
            if (j == 0) {
              if(startDayCount == today.getDate()) {
                calHtml += `<div style='background-color: #FFB3BB;' class='calendar__day horizontalGutter div_can_click' id="${ year }-${ month }-${ startDayCount }">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else {
                calHtml += `<div style='background-color: #BBFFC9;' class='calendar__day horizontalGutter div_can_click' id="${ year }-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
            }
            else if (j == 6) {
              if(startDayCount == today.getDate()) {
                calHtml += `<div style='background-color: #FFB3BB;' class='calendar__day div_can_click' id="${ year }-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else {
                calHtml += `<div style='background-color: #BBFFC9;' class='calendar__day div_can_click' id="${ year }-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
            }
            else {
              if(startDayCount == today.getDate()) {
                calHtml += `<div style='background-color: #FFB3BB;' class='calendar__day horizontalGutter div_can_click' id="${ year }-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else {
                calHtml += `<div style='background-color: #BBFFC9;' class='calendar__day horizontalGutter div_can_click' id="${ year }-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
            }
          }
          
          // 이번달 시작 & 첫 주 && 1일 제외
          else if (i == 0 && j > firstDayName) {
            if (j == 0) {
              if(startDayCount > today.getDate()) {
                calHtml += `<div style='background-color: #BBFFC9' class='calendar__day horizontalGutter '>
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else if(startDayCount == today.getDate()) {
                calHtml += `<div style='background-color: #FFB3BB' class='calendar__day horizontalGutter div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else {
                calHtml += `<div style='background-color: #BBFFC9' class='calendar__day horizontalGutter div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
            }
            else if (j == 6) {
              if(startDayCount > today.getDate()) {
                calHtml += `<div style='background-color: #BBFFC9' class='calendar__day'>
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else if(startDayCount == today.getDate()) {
                calHtml += `<div style='background-color: #FFB3BB' class='calendar__day div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else {
                calHtml += `<div style='background-color: #BBFFC9' class='calendar__day div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
            }

            else {
              if(startDayCount > today.getDate()) {
                calHtml += `<div style='background-color: #BBFFC9' class='calendar__day horizontalGutter'>
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else if(startDayCount == today.getDate()) {
                calHtml += `<div style='background-color: #FFB3BB' class='calendar__day horizontalGutter div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else {
                  calHtml += `<div style='background-color: #BBFFC9' class='calendar__day horizontalGutter div_can_click' id="${year}-${month}-${startDayCount}">
                                <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                                <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                                <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                              </div>`;
              }
            }
          }
          
          // 둘째 주 ~ 이번달 마지막날까지
          else if (i > 0 && startDayCount <= lastDay) {
            if (j == 0) {
              if(startDayCount > today.getDate()) {
                calHtml += `<div style='background-color: #BBFFC9;'class='calendar__day horizontalGutter verticalGutter'>
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/></div>`;
              }
              else if(startDayCount == today.getDate()) {
                calHtml += `<div style='background-color: #FFB3BB;'class='calendar__day horizontalGutter verticalGutter div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else {
                calHtml += `<div style='background-color: #BBFFC9;'class='calendar__day horizontalGutter verticalGutter div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                              </div>`;
              }
            }
            else if (j == 6) {
              if(startDayCount > today.getDate()) {
                calHtml += `<div style='background-color: #BBFFC9;'class='calendar__day verticalGutter'>
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                              </div>`;
              }
              else if(startDayCount == today.getDate()) {
                calHtml += `<div style='background-color: #FFB3BB;'class='calendar__day verticalGutter div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else {
                calHtml += `<div style='background-color: #BBFFC9;'class='calendar__day verticalGutter div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                              </div>`;
              }
            }
            else {
              if(startDayCount > today.getDate()) {
                calHtml += `<div style='background-color: #BBFFC9;'class='calendar__day horizontalGutter verticalGutter'>
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                            </div>`;
              }
              else if(startDayCount == today.getDate()) {
                calHtml += `<div style='background-color: #FFB3BB;'class='calendar__day horizontalGutter verticalGutter div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'></span>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                              </div>`;
              }
              else {
                calHtml += `<div style='background-color: #BBFFC9;'class='calendar__day horizontalGutter verticalGutter div_can_click' id="${year}-${month}-${startDayCount}">
                              <p style="margin-bottom: 0; padding-bottom: 0">${startDayCount}</p>
                              <span id='${year}${month}${setFixDayCount(startDayCount++)}'>
                              <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                              </div>`;
              }
            }
          }
          
          // 다음 달(달력상 나머지 공간)
          else if (startDayCount > lastDay) {
            if (j == 0) {
              calHtml += `<div style='background-color:#B9E1FF;' class='calendar__day horizontalGutter verticalGutter'>
                            <p style="margin-bottom: 0; padding-bottom: 0">${lastDayCount++}</p>
                            <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                          </div>`;
            } else if (j == 6) {
              calHtml += `<div style='background-color:#B9E1FF;' class='calendar__day verticalGutter'>
                            <p style="margin-bottom: 0; padding-bottom: 0">${lastDayCount++}</p>
                            <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                          </div>`;
            } else {
              calHtml += `<div style='background-color:#B9E1FF;' class='calendar__day horizontalGutter verticalGutter'>
                            <p style="margin-bottom: 0; padding-bottom: 0">${lastDayCount++}</p>
                            <img src="${ stamp }" style="width: 30px; height: 30px; margin-bottom: 0; padding-bottom: 0"/>
                          </div>`;
            }
          }
        }
      } // end for


      document.querySelector("#calendar").insertAdjacentHTML("beforeend", calHtml);
    };

    const setFixDayCount = (number) => {
      let fixNum = "";
      if (number < 10) {
        fixNum = "0" + number;
      } else {
        fixNum = number;
      }
      return fixNum;
    };

    if (today.getMonth() + 1 < 10) {
      setCalendarData(today.getFullYear(), "0" + (today.getMonth() + 1));
    } else {
      setCalendarData(today.getFullYear(), "" + (today.getMonth() + 1));
    }

    $(document).on('click', '.div_can_click', function(e) {
      let target = e.target
      let targetTagName = target.tagName

      let clickedDate = ''

      if(targetTagName == 'P') {
        let parent = target.parentNode
        clickedDate = parent.getAttribute('id')

      } else if(targetTagName == 'IMG') {
        let parent = target.parentNode
        clickedDate = parent.getAttribute('id')
      } else if(targetTagName == 'DIV') {
        clickedDate = target.getAttribute('id')
      }

      let strs = clickedDate.split("-")
      strs[1] = strs[1] >= 10 ? strs[1] : '0' + strs[1]
      strs[2] = strs[2] >= 10 ? strs[2] : '0' + strs[2]

      clickedDate = strs[0] + "-" + strs[1] + "-" + strs[2]

      let idx = Number(strs[2])

      // 전체 시간
      // let totaltime = this.gameRecords[idx-1].totaltime
      // console.log(totaltime)

      // 손목 터치 게임(time, score)
      // let wristTouchGameTime = this.gameRecords[idx-1].record[0].time
      // let wristTouchGameScore = this.gameRecords[idx-1].record[0].score
      // console.log(wristTouchGameTime + ", " + wristTouchGameScore)
      
      // 스네이크 게임(time, score)
      // let snakeGameTime = this.gameRecords[idx-1].record[1].time
      // let snakeGameScore = this.gameRecords[idx-1].record[1].score
      // console.log(snakeGameTime + ", " + snakeGameScore)
      
      // 점프 게임(time, score)
      // let jumpGameTime = this.gameRecords[idx-1].record[2].time
      // let jumpGameScore = this.gameRecords[idx-1].record[2].score
      // console.log(jumpGameTime + ", " + jumpGameScore)

      let divContent =
        `
          <h1>${ clickedDate }</h1>
          <hr>
          <h2>총 운동시간 : </h2><br>
          <h3>손목 터치 게임 : 총 스코어 </h3>
          <h3>스네이크 게임 :  총 스코어 </h3>
          <h3>점프 게임 :  총 스코어 </h3><br>
        `

      $('#modal_content').empty()
      $('#modal_content').append(divContent)
      // console.log(divContent)
      modal('my_modal');
    })

    function modal(id) {
    var zIndex = 9999;
    var modal = $('#' + id);

    // 모달 div 뒤에 희끄무레한 레이어
    var bg = $('<div>')
        .css({
            position: 'fixed',
            zIndex: zIndex,
            left: '0px',
            top: '0px',
            width: '100%',
            height: '100%',
            overflow: 'auto',
            // 레이어 색갈은 여기서 바꾸면 됨
            backgroundColor: 'rgba(0,0,0,0.4)'
        })
        .appendTo('body');

    modal
        .css({
            position: 'fixed',
            boxShadow: '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)',

            // 시꺼먼 레이어 보다 한칸 위에 보이기
            zIndex: zIndex + 1,

            // div center 정렬
            top: '50%',
            left: '50%',
            transform: 'translate(-50%, -50%)',
            msTransform: 'translate(-50%, -50%)',
            webkitTransform: 'translate(-50%, -50%)'
        })
        .show()
        // 닫기 버튼 처리, 시꺼먼 레이어와 모달 div 지우기
        .find('.modal_close_btn')
        .on('click', function() {
            bg.remove();
            modal.hide();
        });
}
  },

  methods: {
    ...mapActions(['getRecords']),

    test() {
      alert('test')
      console.log("test")
    },
  }
};
</script>

<style>
html {
  height: 100%;
}

body {
  height: 100%;
  margin: 0;
  position: relative;
}

#calendar {
  height: 99%;
  box-sizing: border-box;
  padding: 0.5%;
}

.calendar__day {
  display: inline-block;
  vertical-align: bottom;
  width: calc(97% / 7);
  height: calc(98% / 5);
  box-sizing: border-box;
  border-radius: 5px;
  /* padding: 20px; */
  padding-top: 5px;
}

.div_can_click {
  cursor: pointer;
}

.horizontalGutter {
  margin-right: 0.5%;
}

.verticalGutter {
  margin-top: 0.5%;
}

#my_modal {
  display: none;
  width: 300px;
  padding: 20px 60px;
  background-color: #fefefe;
  border: 1px solid #888;
  border-radius: 3px;
}

/* #my_modal .modal_close_btn {
  position: absolute;
  top: 10px;
  right: 10px;
} */
</style>
