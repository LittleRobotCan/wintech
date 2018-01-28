if __name__ == '__main__':
    import pandas as pd
    df = pd.read_csv('private_data/one_word_describe.csv')
    word_clean = []
    color_clean = []
    for index, row in df.iterrows():
        word_clean.append(row['Word'].lower())
        color_clean.append(row['Colour'].lower())
    df['color_clean'] = color_clean
    df['word_clean'] = word_clean

    from collections import Counter
    positive = Counter(df[df['color_clean'].isin(["red"])]['word_clean'].tolist())
    negative = Counter(df[df['color_clean'].isin(["green"])]['word_clean'].tolist())
    positive_p = Counter(df[df['color_clean'].isin(["yellow"])]['word_clean'].tolist())
    negative_p = Counter(df[df['color_clean'].isin(["blue"])]['word_clean'].tolist())

    for k, v in positive.most_common(5):
        print '%s: %i' % (k, v)
    for k, v in negative.most_common(5):
        print '%s: %i' % (k,v)


    for k, v in positive_p.most_common(5):
        print '%s: %i' % (k, v)
    for k, v in negative_p.most_common(5):
        print '%s: %i' % (k,v)
    """
    sentiment labels seem off. half of "growing" labeled positive and the other half labeled negative
    """


    industry_all = Counter(df[df['color_clean'].isin(["red","green"])]['word_clean'].tolist())
    personal_all = Counter(df[df['color_clean'].isin(["yellow","blue"])]['word_clean'].tolist())

    for k, v in industry_all.most_common(15):
        print '%s: %i' % (k, v)
    for k, v in personal_all.most_common(15):
        print '%s: %i' % (k,v)

    output = []
    for k, v in industry_all.most_common(len(industry_all)):
        output.append([k,v,"industry"])
    for k, v in personal_all.most_common(len(personal_all)):
        output.append([k,v,"personal"])
    output_df = pd.DataFrame(output, columns = ["word","count", "category"])
    output_df.to_csv("private_data/processed_one_word_describe.csv")

    # ======================================================================= #

    # load the csv files
    labeled_df = pd.read_csv("private_data/processed_one_word_describe.csv", index_col=0)
    print sum(labeled_df[(labeled_df['category']=="industry")&(labeled_df['sentiment']=="p")]["count"])
    # 454
    print sum(labeled_df[(labeled_df['category']=="industry")&(labeled_df['sentiment']=="-")]["count"])
    #207

    print sum(labeled_df[(labeled_df['category'] == "personal") & (labeled_df['sentiment'] == "p")]["count"])
    #374
    print sum(labeled_df[(labeled_df['category'] == "personal") & (labeled_df['sentiment'] == "-")]["count"])
    #241


    labeled_df = labeled_df.sort_values(by="count", ascending=False)
    labeled_df[(labeled_df['category']=="industry")&(labeled_df['sentiment']=="p")][:10]
    labeled_df[(labeled_df['category'] == "industry") & (labeled_df['sentiment'] == "-")][:20]

    labeled_df[(labeled_df['category']=="personal")&(labeled_df['sentiment']=="p")][:10]
    labeled_df[(labeled_df['category'] == "personal") & (labeled_df['sentiment'] == "-")][:20]