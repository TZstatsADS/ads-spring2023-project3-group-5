def encoding(LabelEncoder, to_categorical, num_classes, train, test=None):
    # encode labels as integers
    le = LabelEncoder()
    y_train_int = le.fit_transform(train)
    label_map = {le.transform([label])[0]: label for label in train}

    if test is not None:
        y_test_int = le.transform(test)
        # convert integer-encoded labels to one-hot encoded format
        y_test = to_categorical(y_test_int, num_classes)
    else:
        y_test = None

    # convert integer-encoded labels to one-hot encoded format
    y_train = to_categorical(y_train_int, num_classes)
    
    if y_test is not None:
        return y_train, y_test
    else:
        return y_train, None