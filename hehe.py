import numpy as np
arr1 = np.array([1, 2, 3, 4, 5])
np.zeros((3, 3))  # Mảng 3x3 toàn số 0
np.ones((2, 2))   # Mảng 2x2 toàn số 1
np.full((2, 3), 7)  # Mảng 2x3 toàn số 7
np.eye(4)  # Ma trận đơn vị 4x4
np.arange(0, 10, 2)  # [0 2 4 6 8]
np.linspace(0, 1, 5)  # [0. 0.25 0.5 0.75 1.]
np.random.rand(2, 3)  # Mảng 2x3 số ngẫu nhiên từ 0 đến 1
np.random.randint(1, 10, (3, 3))  # Mảng 3x3 số nguyên từ 1 đến 9
np.random.randn(3, 3)  # Mảng 3x3 phân phối chuẩn
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2[0, 1])  # Truy cập phần tử dòng 0, cột 1 (kết quả: 2)
print(arr2[:, 1])  # Lấy cột thứ 2 (kết quả: [2 5])
arr2.reshape(2, 3)  # Thay đổi thành 2 hàng, 3 cột
arr2.flatten()  # Trả về mảng 1D (copy)
arr2.ravel()  # Trả về mảng 1D (view)
arr2.T  # Chuyển vị
arr2.swapaxes(0, 1)  # Đổi trục
arr1 + arr2  # Cộng
arr1 - arr2  # Trừ
arr1 * arr2  # Nhân phần tử
arr1 / arr2  # Chia phần tử
arr2 ** 2  # Bình phương từng phần tử
np.sqrt(arr2)  # Căn bậc hai
np.sum(arr)  # Tổng các phần tử
np.mean(arr)  # Giá trị trung bình
np.min(arr)  # Giá trị nhỏ nhất
np.max(arr)  # Giá trị lớn nhất
np.argmin(arr)  # Chỉ số phần tử nhỏ nhất
np.argmax(arr)  # Chỉ số phần tử lớn nhất
np.dot(A, B)  # Tích ma trận
np.linalg.det(A)  # Định thức ma trận
np.linalg.inv(A)  # Ma trận nghịch đảo
np.linalg.eig(A)  # Giá trị riêng & vector riêng
np.concatenate((arr1, arr2), axis=0)  # Ghép theo hàng
np.vstack((arr1, arr2))  # Ghép dọc
np.hstack((arr1, arr2))  # Ghép ngang
np.split(arr, 2)  # Chia mảng làm 2 phần
np.hsplit(arr, 2)  # Chia theo cột
np.vsplit(arr, 2)  # Chia theo hàng
arr[arr > 5]  # Lấy các phần tử lớn hơn 5
np.where(arr % 2 == 0, "Chẵn", "Lẻ")  # Thay số chẵn/lẻ
np.save("data.npy", arr)  # Lưu mảng vào file
arr = np.load("data.npy")  # Tải mảng từ file
np.savetxt("data.csv", arr, delimiter=",")  # Lưu dưới dạng CSV
arr = np.loadtxt("data.csv", delimiter=",")  # Đọc file CSV
