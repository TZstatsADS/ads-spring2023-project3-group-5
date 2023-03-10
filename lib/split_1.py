def model_1_split(n_img, n_noisy, imgs, noisy_labels, clean_labels, np, train_test_split):
    
    n_clean_noisy = n_img - n_noisy
    noisy = np.empty(n_img)
    clean = np.empty(n_clean_noisy)
        
    for i in range(n_img):
        # The target vector consists of noisy labels
        noisy[i] = noisy_labels[i]
        
    for i in range(n_clean_noisy):
        # The target vector consists of clean labels
        clean[i] = clean_labels[i]
        
    noisy = noisy[-40000:]
    target_vec = np.concatenate((clean, noisy), axis=None)

    result = train_test_split(imgs, target_vec, test_size=0.10, random_state=42)
    return result