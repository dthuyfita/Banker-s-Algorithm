# Giải thuật Chủ nhà băng

import numpy as np

# Hàm kiểm tra an toàn
def isSafe(proc, avail, maxx, alloc):            
        # Tính ma trận need
        need = maxx - alloc

        #Hiển thị bảng
        print("  Max           Allocation" + "        Need" +
                                              "           Available")
        print(maxx[0], "\t", alloc[0], "\t", need[0], "\t", avail)
        for i in range (P):
                if(i>0):
                        print(maxx[i], "\t", alloc[i], "\t", need[i])

        # Giả sử tất cả các tiến trình đã đc finish
        finish = [0] * P #khởi tạo finish[i] = alloc(i)==0, i=1,2,...,n
        
        # khởi tạo chuỗi an toàn
        safeSeq = [0] * P

        #khởi tạo work:=avail
        work = [0] * R
        for i in range(R):
                work[i] = avail[i] 

        # While các tiến trình chưa finish
        count = 0 #biến đếm để cho vào chuỗi an toàn
        while (count < P):
                
                # Tìm proc(i) chưa kết thúc và có nhu cầu k vượt quá khả dụng
                found = False #giả sử chưa tìm thấy
                for p in range(P):
                
                        # Check xem finish chưa, chưa thì làm tiếp
                        if (finish[p] == 0):
                        
                                # Ktra xem Need của proc này có vượt quá Work ko
                                for j in range(R):
                                        if (need[p][j] > work[j]):
                                                break #vượt quá thì thôi =)))
                                        
                                # nếu proc này thỏa mãn Need <= Work
                                if (j == R - 1):
                                
                                        # Lượng khả dụng đc cộng thêm số tài nguyên phân phối
                                        #cho proc(i) vì proc này đã có đủ tài nguyên để thực hiện, rồi kết thúc.
                                        for k in range(R):
                                                work[k] += alloc[p][k]

                                        # Thêm proc này vào chuỗi an toàn
                                        safeSeq[count] = p
                                        count += 1

                                        # Đánh dấu finish[i] = true
                                        finish[p] = 1


                                        found = True
                                        
 

                # Nếu k tìm thấy proc nào đáp ứng yc
                if (found == False):
                        print("Hệ thống không ở trạng thái an toàn.")
                
                        return False
                        
        # Nếu hệ thống ở trạng thái an toàn thì in ra chuỗi an toàn
        print("Hệ thống đang ở trạng thái an toàn.",
                        "\nChuỗi an toàn là: ", end = " ")
        print(*safeSeq)

        return True


# Driver code
if __name__ =="__main__":
        # Số tiến trình
        P = 4
        # Số loại tài nguyên
        R = 3
        
        proc = np.array([0,1,2,3])

        #Nhập W hệ có
        W = np.array([5,5,7])

        # nhập Maximum 
        maxx = np.array([[7,5,3],[3,2,2],[9,0,2],[2,2,2]])

        # nhập Allocation
        alloc = np.array([[0,1,0],[2,0,0],[3,0,2],[0,0,2]])
        
        # tính Available
        #avail = np.array([1])
        sum =(np.sum(alloc, axis = 0))
        avail = W - sum

        # Hàm ktra an toàn
        isSafe(proc, avail, maxx, alloc)
