# example workflow:
# $ python -i main.py
# # now you can work with hvdf dataframe
# >>> print(hvdf)
# # find some chars:
# >>> find_char('中')
# char             中
# hanviet    [trung]
# pinyin      zhong1
# Name: 4, dtype: object
# char             中
# hanviet    [trúng]
# pinyin      zhong4
# Name: 5, dtype: object
# # Look at the number after "Name: ". Now get an entry by index to edit:
# >>> get_hanviet_of_index(5)[0] = 'abcxxx'
# # after finishing edit, save the dataframe to csv
# >>> save_hanviet_csv()
# optional: export to .js file
# >>> export_to_js("hanvietData.js")

import pandas as pd
import json

CHINESE_UNICODE_RANGE = [
    (0x4E00, 0x9FFF),
    (0x3400, 0x4DBF),
    (0x20000, 0x2A6DF),
    (0x2A700, 0x2B73F),
    (0x2B740, 0x2B81F),
    (0x2B820, 0x2CEAF),
    (0x2CEB0, 0x2EBEF),
    (0x30000, 0x3134F),
    (0x31350, 0x323AF),
    (0xF900, 0xFAFF),
    (0x2F800, 0x2FA1F),
    (0x3007, 0x3007),
]

def is_chinese_unicode(char):
    if char:
        code = ord(char)
        for start, end in CHINESE_UNICODE_RANGE:
            if start <= code <= end:
                return True
    return False

def check_pinyin_sanity(pinyin):
    # TODO: remove the '*' condition
    return isinstance(pinyin, str) and (pinyin == '*' or (pinyin.islower() and pinyin.replace('u:','v').isalnum()))

def check_hanviet_df_sanity(df):
    assert set(df.columns) == {'char', 'hanviet', 'pinyin'}
    assert not df.duplicated(subset=['char', 'pinyin']).any()
    assert df['hanviet'].apply(lambda x: isinstance(x, list)).all()
    assert df['char'].apply(lambda x: is_chinese_unicode(x)).all()
    assert df['pinyin'].apply(lambda x: check_pinyin_sanity(x)).all()

def load_hanviet_csv(name):
    df = pd.read_csv(name + '.csv', keep_default_na=False)
    df['hanviet']=df['hanviet'].str.replace("'", '"').apply(json.loads)
    check_hanviet_df_sanity(df)
    return df

hvdf = load_hanviet_csv('hanviet')

def save_csv(df, name):
    check_hanviet_df_sanity(df)
    df.to_csv(name + '.csv', index=False)

def save_hanviet_csv():
    save_csv(hvdf, 'hanviet')

def find_char(trad_char):
    try:
        group = hvdf.groupby('char').get_group(trad_char)
        for index, row in group.iterrows():
            print(row)
        return True
    except KeyError:
        print(f"Char value {trad_char} not found")
        return False

def get_hanviet_of_index(index):
    return hvdf.iloc[index]['hanviet']

def prepare_hanviet_json_str(df):
    hanviet_data = {}
    for _, row in df.iterrows():
        if row['char'] not in hanviet_data:
            hanviet_data[row['char']] = {}
        
        hanviet_data[row['char']][row['pinyin']] = row['hanviet']
    json_str = json.dumps(hanviet_data, indent=0, ensure_ascii=False)
    return json_str

def export_to_js(path='../hanviet-pinyin-words/src/hanvietData.js'):
    check_hanviet_df_sanity(hvdf)
    json_str = prepare_hanviet_json_str(hvdf)
    with open(path, 'w', encoding='utf-8') as f:
        f.write('export const hanvietData = ')
        f.write(json_str)