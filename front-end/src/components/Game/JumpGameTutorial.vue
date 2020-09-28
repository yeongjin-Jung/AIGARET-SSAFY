<template>
  <transition name="modal" appear>
    <div class="modal modal-overlay" @click.self="$emit('close')" >
      <div class="modal-window" style="width : 80vw; height: 80vh; background-color : rgba(255,255,255,1); ">
        <div class="modal-content" style="max-width : 100%; height: 70vh;">
          <slot/>
        </div>
        <footer class="modal-footer"  style="height: 10vh;">
          <slot name="footer" >
          </slot>
        </footer>
      </div>
    </div>
  </transition>
</template>

<style lang="stylus" scoped>
.modal {
  &.modal-overlay {
    display: flex;
    align-items: center;
    justify-content: center;
    position: fixed;
    z-index: 30;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
  }

  &-window {
    background: #fff;
    border-radius: 4px;
    overflow: hidden;
  }

  &-content {
    padding: 10px 20px;
  }

  &-footer {
    background-color : rgba(0,0,0,0);
    padding: 10px;
    text-align: center;
  }
}

.modal-enter-active, .modal-leave-active {
  transition: opacity 0.4s;

  .modal-window {
    transition: opacity 0.4s, transform 0.4s;
  }
}

.modal-leave-active {
  transition: opacity 0.6s ease 0.4s;
}

.modal-enter, .modal-leave-to {
  opacity: 0;

  .modal-window {
    opacity: 0;
    transform: translateY(-20px);
  }
}

.modal-enter-active {
  animation: modal-in .5s;
}
.modal-leave-active {
  animation: modal-in .5s reverse;
}
@keyframes modal-in {
  0% {
    transform: scale(0);
  }
  50% {
    transform: scale(1.1);
  }
  100% {
    transform: scale(1);
  }
}
</style>
