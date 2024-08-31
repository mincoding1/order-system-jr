import axios from "axios";

export const DOMAIN = "http://localhost:8000";
//export const DOMAIN = "http://3.37.88.111:8000"

const request = axios.create({
  baseURL: `${DOMAIN}/api/v1`,
});

export const api = {
  menus: {
    findAll: () => request.get("/menus"),
    findOne: (id) => request.get(`/menus/${id}`),

    create: (name, description, image_src) => {
      const formData = new FormData();
      formData.append("name", name);
      formData.append("description", description);
      formData.append("image_src", image_src);
      return request.post(`/menus/`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
    },
    // 메뉴 수정
    update: (id, name, description, image_src) =>
      request.patch(`/menus/${id}`, {
        name: name,
        description: description,
        image_src: image_src,
      }),

    // 메뉴 이미지 수정
    updateImage: (file) => {
      const formData = new FormData();
      formData.append("file", file);
      return request.post(`/menus/create/image/`, formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
    },
    // 메뉴 삭제
    delete: (id) => request.delete(`/menus/${id}`),
  },

  orders: {
    // 주문목록 조회
    findAll: () => request.get("/orders"),
    // 주문 조회
    findOne: (id) => request.get(`/orders/${id}`),
    // 주문하기
    create: (menus_id, quantity, request_detail) =>
      request.post(`/orders/`, {
        menus_id: menus_id,
        quantity: quantity,
        request_detail: request_detail,
      }),
    // 주문 내역 수정하기
    update: (id, menus_id, quantity, request_detail) =>
      request.patch(`/orders/${id}`, {
        menus_id: menus_id,
        quantity: quantity,
        request_detail: request_detail,
      }),
    // 주문 내역 삭제하기
    delete: (id) => request.delete(`/orders/${id}`),
  },
};
