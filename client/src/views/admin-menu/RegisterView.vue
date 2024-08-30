<script setup>
import { ref } from "vue";
import { useCommonStore } from "@/stores/common";
import { useRoute, useRouter } from "vue-router";
import { api } from "@/utils/axios";

const route = useRoute();
const router = useRouter();
const common = useCommonStore();

const name = ref("");
const description = ref("");
const file = ref(null);
const originFileName = ref("");

function fileChange(e) {
  console.log(e.target.files);
  file.value = e.target.files[0];
}

async function menuCreate() {
  if (!name.value || !description.value || !file.value) {
    alert("빈 값이 있습니다. 내용을 전부 작성해주세요.");
  }
  const fileResult = await api.menus.updateImage(file.value);
  await api.menus.create(
    name.value,
    description.value,
    fileResult.data.filename
  );
  alert("메뉴가 생성되었습니다.");
  router.push({ name: "menus" });
}

function setURL(file) {
  const imageURL = URL.createObjectURL(file);
  return imageURL;
}

async function menuUpdate() {
  const result = await api.menus.update(
    route.params.id,
    name.value,
    description.value,
    originFileName.value
  );
  alert("수정 성공");
  router.push({
    name: "menus-detail",
    params: { id: result.id },
  });
}
async function updateImage() {
  const fileResult = await api.menus.updateImage(file.value);
  await api.menus.update(
    route.params.id,
    name.value,
    description.value,
    fileResult.data.filename
  );
  alert("이미지 수정 성공");
}

async function getMenu() {
  const result = await api.menus.findOne(route.params.id);
  name.value = result.data.name;
  description.value = result.data.description;
  originFileName.value = result.data.image_src;
}

if (route.params.id) {
  common.changeTitle("메뉴 수정하기");
  getMenu();
} else {
  common.changeTitle("메뉴 추가하기");
}
</script>

<template>
  <div class="form-wrapper">
    <div>
      <span>메뉴 이름: </span>
      <input type="text" v-model="name" />
    </div>
    <div>
      <span>메뉴 설명: </span>
      <input type="text" v-model="description" />
    </div>
    <input type="file" @change="fileChange" />
    <div v-if="route.params.id">
      <button @click="menuUpdate">메뉴 수정하기</button>
      <button @click="updateImage">이미지 수정하기</button>
    </div>
    <div v-else>
      <button @click="menuCreate">메뉴 추가하기</button>
    </div>
  </div>
  <div class="image-wrapper" v-if="file">
    <img class="selected-image" :src="setURL(file)" />
  </div>
</template>

<style scoped>
.form-wrapper {
  display: flex;
  flex-direction: column;
  margin-top: 50px;
  border: 1px solid black;
  padding: 20px;
}
.form-wrapper > * {
  margin: 10px;
}
.image-wrapper {
  margin-top: 30px;
}
</style>
