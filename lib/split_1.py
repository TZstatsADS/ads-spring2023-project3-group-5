def model_1_split(n_img,imgs,noisy_labels, np, train_test_split):
    
    target_vec = np.empty(n_img)

    for i in range(n_img):
        # The target vector consists of noisy labels
        target_vec[i] = noisy_labels[i]

    result = train_test_split(imgs, target_vec, test_size=0.30, random_state=42)
    return result
