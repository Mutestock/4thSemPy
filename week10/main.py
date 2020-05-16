import cli

if __name__ == "__main__":
    cli.manager()


'''
Exercise meanshift
Exercise 1 understand the titanic data example

Understand the Titanic clustering example

    Look at this https://github.com/datsoftlyngby/dat4sem2020spring-python/blob/master/notebooks/10-4-2%20Clustering%20Titanic%20example.ipynb
    Go through the code and make sure you understand everything

Exercise 2 use meanshift on the iris dataset

    load 'iris_data.csv' into a dataframe
    get unique labels (Species column)
    plot with a scatter plot each iris flower sample colored by label (3 different colors)
    use: MeanShift and estimate_bandwidth from sklearn.cluster to first estimate bandwidth and then get the clusters (HINT: estimate_bandwidth() takes an argument: quantile set it to 0.2 for best result
    print out labels, cluster centers and number of clusters (as returned from the MeanShift function
    create a new scatter plot where each flower is colored according to cluster label
    add a dot for the cluster centers
    Compare the 2 plots (colored by actual labels vs. colored by cluster label)

'''