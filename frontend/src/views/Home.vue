<template>
  <v-row>
    <v-col cols="2">
      <v-navigation-drawer permanent>
        <v-list-item>
          <v-list-item-title>AIGARET</v-list-item-title>
        </v-list-item>

        <v-divider></v-divider>

        <v-list>
          <v-list-group
            v-for="item in items"
            :key="item.title"
            v-model="item.active"
            no-action
            sub-group
          >
            <template v-slot:activator>
              <v-list-item-title v-text="item.title"></v-list-item-title>
            </template>
            <v-list-item
              v-for="subItem in item.subItems"
              :key="subItem.title"
            >
              <v-list-item-content>
                <v-list-item-title v-text="subItem.title"></v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </v-list-group>
        </v-list>
      </v-navigation-drawer>
    </v-col>
    <v-col>
      <Game />
    </v-col>
  </v-row>
</template>

<script>
import Game from '../components/Game/Game.vue'

export default {
  name: 'Home',
  components: {
    Game
  },
  data () {
    return {
      items: [
        {
          title: '팔 뻗기',
          active: true,
          subItems: [
            { title: '게임 1' },
            { title: '게임 2' },
            { title: '게임 3' },
          ],
        },
        {
          title: '균형 잡기',
          active: true,
          subItems: [
            { title: '게임 1' },
            { title: '게임 2' },
            { title: '게임 3' },
          ],
        },
        {
          title: '근력 운동',
          active: true,
          subItems: [
            { title: '게임 1' },
            { title: '게임 2' },
            { title: '게임 3' },
          ],
        }
      ],
    }
  },
}
</script>
