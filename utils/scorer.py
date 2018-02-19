import sklearn


def report_score(gold_labels, predicted_labels):
    score = sklearn.metrics.f1_score(gold_labels, predicted_labels, average='macro')
    print("macro-F1: {:.2f}".format(score))
    # for a more detailed report (and average F1 score) uncomment this line
    # print (sklearn.metrics.classification_report(gold_labels, predicted_labels))
