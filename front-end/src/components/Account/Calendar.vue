<template>
  <v-sheet>
    <v-toolbar flat color="white">

      <!-- <v-btn outlined class="mr-4" color="grey darken-2" @click="setToday"
        >Today</v-btn
      > -->

      <v-spacer></v-spacer>

      <!-- <v-btn fab text small color="grey darken-2" @click="prev">
        <v-icon small>mdi-chevron-left</v-icon>
      </v-btn> -->

      <v-toolbar-title v-if="$refs.calendar">{{ $refs.calendar.title }}</v-toolbar-title>
      
      <!-- <v-btn fab text small color="grey darken-2" @click="next">
        <v-icon small>mdi-chevron-right</v-icon>
      </v-btn> -->

      <v-spacer></v-spacer>

      <!-- <v-menu bottom right>
        <template v-slot:activator="{ on, attrs }">
          <v-btn outlined color="grey darken-2" v-bind="attrs" v-on="on">
            <span>{{ typeToLabel[type] }}</span>
            <v-icon right>mdi-menu-down</v-icon>
          </v-btn>
        </template>
        <v-list>
          <v-list-item @click="type = 'day'">
            <v-list-item-title>Day</v-list-item-title>
          </v-list-item>
          <v-list-item @click="type = 'week'">
            <v-list-item-title>Week</v-list-item-title>
          </v-list-item>
          <v-list-item @click="type = 'month'">
            <v-list-item-title>Month</v-list-item-title>
          </v-list-item>
          <v-list-item @click="type = '4day'">
            <v-list-item-title>4 days</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu> -->
    </v-toolbar>

    <v-calendar ref="calendar" v-model="focus" color="primary" :type="type" :events="events" :event-color="getEventColor" @change="updateRange"></v-calendar>

  </v-sheet>
</template>

<script>
export default {
  name: "Calendar",

  data: () => ({
    calendarTitle: '',
    focus: "",
    type: 'month',
    typeToLabel: {
      month: 'Month',
      week: 'Week',
      day: 'Day',
      '4day': '4 Days'
    },
    selectedEvent: {},
    selectedElement: null,
    selectedOpen: false,
    events: [],
    colors: [
      "blue",
      "indigo",
      "deep-purple",
    ],
    names: [
      "10분 이상",
      "30분 이상",
      "60분 이상",
    ],
  }),

  mounted() {
    console.log("Calendar.vue mounted.")
    console.log("this.$refs.calendar", this.$refs.calendar)
    this.$refs.calendar.checkChange();
    console.log(this.$refs.calendar.title)
  },

  methods: {
    viewDay({ date }) {
      this.focus = date;
      this.type = "day";
    },

    getEventColor(event) {
      return event.color;
    },

    setToday() {
      this.focus = "";
    },

    prev() {
      this.$refs.calendar.prev();

      const strs = this.$refs.calendar.title.split(" ")
      console.log(strs[0] + ", " + strs[1])
      this.calendarTitle = strs[1] + "년 " + strs[0]
    },

    next() {
      this.$refs.calendar.next();

      const strs = this.$refs.calendar.title.split(" ")
      console.log(strs[0] + ", " + strs[1])
      this.calendarTitle = strs[1] + "년 " + strs[0]
    },

    showEvent({ nativeEvent, event }) {
      const open = () => {
        this.selectedEvent = event;
        this.selectedElement = nativeEvent.target;
        setTimeout(() => (this.selectedOpen = true), 10);
      };

      if (this.selectedOpen) {
        this.selectedOpen = false;
        setTimeout(open, 10);
      } else {
        open();
      }

      nativeEvent.stopPropagation();
    },

    updateRange ({ start, end }) {
      // start : 해당 월의 시작 일수(1일)
      // end : 해당 월의 끝 일수(28~31일)

      const events = []

      const min = new Date(`${start.date}T00:00:00`)
      const max = new Date(`${end.date}T23:59:59`)
      console.log("min : ", min)
      console.log("max : ", max)

      const days = (max.getTime() - min.getTime()) / 86400000
      console.log("days : ", days)

      const eventCount = this.rnd(days, days + 20)
      // eventCount가 해당 월에 해당하는 로우를 다 받아옴. 로우의 개수가 될 것.

      for (let i = 0; i < eventCount; i++) {
        const allDay = this.rnd(0, 3) === 0

        const firstTimestamp = this.rnd(min.getTime(), max.getTime())
        const first = new Date(firstTimestamp - (firstTimestamp % 900000))

        const secondTimestamp = this.rnd(2, allDay ? 288 : 8) * 900000
        const second = new Date(first.getTime() + secondTimestamp)

        let idx = this.rnd(0, this.names.length - 1)
        events.push({
          name: this.names[idx],
          start: first,
          // end: second,
          color: this.colors[idx],
          // timed: !allDay
        })
      }

      this.events = events
    },

    rnd(a, b) {
      return Math.floor((b - a + 1) * Math.random()) + a;
    },
  },
};
</script>

<style>
</style>