def model_split(n_img, n_noisy, imgs, noisy_labels, clean_labels, np, random):
    
    n_clean_noisy = n_img - n_noisy
    noisy = np.empty(n_img)
    clean = np.empty(n_clean_noisy)
    n_val = round(n_clean_noisy*0.1)
        
    for i in range(n_img):
        # The target vector consists of noisy labels
        noisy[i] = noisy_labels[i]
        
    for i in range(n_clean_noisy):
        # The target vector consists of clean labels
        clean[i] = clean_labels[i]
    
    random.seed(42)
    ind = random.sample(range(1, n_clean_noisy), n_val)
    
    a_img_matrix_clean=imgs[0:n_clean_noisy]
    a_clean_labels_clean=clean[0:n_clean_noisy]
    a_noisy_labels_clean=noisy[0:n_clean_noisy]
    
    #9000
    a_img_matrix_train = np.delete(a_img_matrix_clean, ind, 0)
    a_clean_labels_train = np.delete(a_clean_labels_clean, ind)
    a_noisy_labels_train = np.delete(a_noisy_labels_clean, ind)
    
    #1000
    img_matrix_test = np.take(a_img_matrix_clean, ind, 0)
    clean_labels_test = np.take(a_clean_labels_clean, ind)
    noisy_labels_test = np.take(a_noisy_labels_clean, ind)

    #49000
    b_img_matrix_train = np.delete(imgs, ind, 0)
    b_noisy_labels_train = np.delete(noisy, ind, 0)
    
    return a_img_matrix_train, a_clean_labels_train, a_noisy_labels_train, img_matrix_test, clean_labels_test, noisy_labels_test, b_img_matrix_train, b_noisy_labels_train