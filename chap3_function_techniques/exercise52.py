from utils2 import cal_vec_norm


def norm_vec(vec):
    vec_norm = cal_vec_norm(vec)

    vec = vec.copy()
    for idx in range(len(vec)):
        vec[idx] /= vec_norm
    return vec


u = [1, 2, 3]
u_norm = cal_vec_norm(vec=u)
print(f"norm before normalization: {u_norm:.2f}")

u_ = norm_vec(vec=u)
u_norm_ = cal_vec_norm(vec=u_)
print(f"norm after normalization: {u_norm_:.2f}")