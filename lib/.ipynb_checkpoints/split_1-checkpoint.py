def model_1_split(imgs,noisy_labels, np, train_test_split):

    # RGB histogram dataset construction
    n_img = 50000
    no_bins = 6
    bins = np.linspace(0,255,no_bins) # the range of the rgb histogram
    target_vec = np.empty(n_img)
    feature_mtx = np.empty((n_img,3*(len(bins)-1)))
    i = 0
    for i in range(n_img):
        # The target vector consists of noisy labels
        target_vec[i] = noisy_labels[i]

        # Use the numbers of pixels in each bin for all three channels as the features
        feature1 = np.histogram(imgs[i][:,:,0],bins=bins)[0] 
        feature2 = np.histogram(imgs[i][:,:,1],bins=bins)[0]
        feature3 = np.histogram(imgs[i][:,:,2],bins=bins)[0]

        # Concatenate three features
        feature_mtx[i,] = np.concatenate((feature1, feature2, feature3), axis=None)
        i += 1

    result = train_test_split(feature_mtx, target_vec, test_size=0.30, random_state=42)
    return result