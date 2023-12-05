def cal_vec_norm(vec):
    vec_norm = 0
    for element in vec:
        vec_norm += element**2
    vec_norm **= 0.5
    return vec_norm

u = [1, 2, 3]
u_norm = cal_vec_norm(u)
print(f"vec norm before normalization: {u_norm:.2f}")

for element_idx in range(len(u)):
    u[element_idx] /= u_norm

u_norm = cal_vec_norm(u)
print(f"vec norm after normalization: {u_norm:.2f}")