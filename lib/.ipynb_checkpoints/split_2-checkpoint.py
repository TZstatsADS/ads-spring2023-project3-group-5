def model_2_split(imgs, noisy_labels, clean_labels, np, random):
    
    # RGB histogram dataset construction
    n_img = 50000
    n_noisy = 40000
    n_clean_noisy = n_img - n_noisy
    no_bins = 6
    bins = np.linspace(0,255,no_bins) # the range of the rgb histogram
    noisy = np.empty(n_img)
    clean = np.empty(n_clean_noisy)
    b_img_matrix_train = np.empty((n_img,3*(len(bins)-1)))
    i = 0
        
    for i in range(n_img):
        # The target vector consists of noisy labels
        noisy[i] = noisy_labels[i]

        # Use the numbers of pixels in each bin for all three channels as the features
        feature1 = np.histogram(imgs[i][:,:,0],bins=bins)[0] 
        feature2 = np.histogram(imgs[i][:,:,1],bins=bins)[0]
        feature3 = np.histogram(imgs[i][:,:,2],bins=bins)[0]

        # Concatenate three features
        b_img_matrix_train[i,] = np.concatenate((feature1, feature2, feature3), axis=None)
        i += 1
        
    for i in range(n_clean_noisy):
        # The target vector consists of noisy labels
        clean[i] = clean_labels[i]
    
    random.seed(42)
    ind = random.sample(range(1, 10000), 3000)
    
    a_img_matrix_train=b_img_matrix_train[0:10000]
    a_clean_labels_train=clean[0:10000]
    a_noisy_labels_train=noisy[0:10000]
    
    #7000
    np.delete(a_img_matrix_train, ind)
    np.delete(a_clean_labels_train, ind)
    np.delete(a_noisy_labels_train, ind)
    
    #3000
    img_matrix_test = [b_img_matrix_train[i] for i in ind]
    clean_labels_test = [clean[i] for i in ind]
    noisy_labels_test = [noisy[i] for i in ind]

    #47000
    np.delete(b_img_matrix_train, ind)
    
    return a_img_matrix_train, a_clean_labels_train, a_noisy_labels_train, img_matrix_test, clean_labels_test, noisy_labels_test, b_img_matrix_train