import numpy as np

def disparity_ssd(L, R):
    """Compute disparity map D(y, x) such that: L(y, x) = R(y, x + D(y, x))

    Params:
    L: Grayscale left image
    R: Grayscale right image, same size as L

    Returns: Disparity map, same size as L, R
    """

    # TODO: Your code here
    row_num = L.shape[0]
    col_num = L.shape[1]
    w_size = 6

    row_num_half = int(w_size/2)
    col_num_half = int(w_size/2)
    disparity = np.zeros((col_num, row_num))
    
    
    for r in range(row_num):
        for c in range(col_num):
            difference = np.zeros(col_num)

            for curr_c in range(col_num):
                diff = 0
                for j in range(w_size):
                    for i in range(w_size):

                        L_x = c + j - col_num_half
                        L_y = r + i - row_num_half

                        R_x = curr_c + j - col_num_half
                        R_y = r + i - row_num_half

                        Rvalue = 0
                        Lvalue = 0
                        if not(L_x < 0 or L_x >= col_num or L_y < 0 or L_y >= row_num):
                            Lvalue = L[L_x][L_y]

                        if not(R_x < 0 or R_x >= col_num or R_y < 0 or R_y >= row_num):
                            Rvalue = R[R_x][R_y]

                        # print(L_x, L_y, R_x, R_y)

                        diff += (Rvalue - Lvalue) ** 2
                difference[curr_c] = diff
                # print(diff)
         
            disparity[r][c] = np.argmin(difference) - c


    return disparity
