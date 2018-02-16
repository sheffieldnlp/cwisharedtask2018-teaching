from utils.dataset import Dataset


if __name__ == '__main__':
    english_data = Dataset('english')
    # spanish_data = Dataset('spanish')

    print("English: {} training - {} dev".format(len(english_data.trainset), len(english_data.devset)))
    # print("Spanish: {} training - {} dev".format(len(spanish_data.trainset), len(spanish_data.devset)))

    for sent in english_data.trainset:
        print(sent['sentence'], sent['target_word'], sent['gold_label'])
