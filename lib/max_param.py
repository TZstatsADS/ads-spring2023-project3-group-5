def hyperparam_max(results, var):
    # extract test accuracies and variables from result dictionaries
    test_accuracies = [result['test_accuracy'] for result in results]
    variables = [result.get(var) for result in results] 

    # find the index of the result with the largest test accuracy
    best_index = test_accuracies.index(max(test_accuracies))

    # extract the variable from the result with the largest test accuracy
    best_var = variables[best_index]

    return best_var