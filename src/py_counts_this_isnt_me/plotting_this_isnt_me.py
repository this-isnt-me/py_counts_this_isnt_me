# Import Packages/Modules
import matplotlib.pyplot as plt

# Function to plot bar chart of n most frequent words
def plot_words(word_counts, n=10):
    """Plot a bar chart of word counts."""
    # get n most common words
    top_n_words = word_counts.most_common(n)
    # unzip most common words and count for each word
    word, count = zip(*top_n_words)
    # create figure with plotted data 
    fig = plt.bar(range(n), count)
    # adjust ticks label on x axis
    plt.xticks(range(n), labels=word, rotation=45)
    # create axis label on x axis
    plt.xlabel("Word")
    # create axis label on y axis
    plt.ylabel("Count")
    # return figure
    return fig