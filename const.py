from todoist_api_python.api import TodoistAPI

TODOIST_API_KEY = "e3b0b2ed0642281f8f775fc954ef1567ea84537c"
todoist_api = TodoistAPI(TODOIST_API_KEY)
tiny_abbreviations={
1: "GN",
2: "EX",
3: "LV",
4: "NU",
5: "DT",
6: "JS",
7: "JG",
8: "RT",
9: "S1",
10: "S2",
11: "K1",
12: "K2",
13: "R1",
14: "R2",
15: "ER",
16: "NH",
17: "ET",
18: "JB",
19: "PS",
20: "PR",
21: "EC",
22: "SS",
23: "IS",
24: "JR",
25: "LM",
26: "EK",
27: "DN",
28: "HS",
29: "JL",
30: "AM",
31: "OB",
32: "JH",
33: "MC",
34: "NM",
35: "HK",
36: "ZP",
37: "HG",
38: "ZC",
39: "ML",
40: "MT",
41: "MK",
42: "LK",
43: "JN",
44: "AC",
45: "RM",
46: "C1",
47: "C2",
48: "GL",
49: "EP",
50: "PP",
51: "CL",
52: "H1",
53: "H2",
54: "T1",
55: "T2",
56: "TT",
57: "PM",
58: "HB",
59: "JM",
60: "P1",
61: "P2",
62: "J1",
63: "J2",
64: "J3",
65: "JD",
66: "RV"
}
Book_names_en={
1: "Genesis",
2: "Exodus",
3: "Leviticus",
4: "Numbers",
5: "Deuteronomy",
6: "Joshua",
7: "Judges",
8: "Ruth",
9: "1 Samuel",
10: "2 Samuel",
11: "1 Kings",
12: "2 Kings",
13: "1 Chronicles",
14: "2 Chronicles",
15: "Ezra",
16: "Nehemiah",
17: "Esther",
18: "Job",
19: "Psalms",
20: "Proverbs",
21: "Ecclesiastes",
22: "Song of Solomon",
23: "Isaiah",
24: "Jeremiah",
25: "Lamentations",
26: "Ezekiel",
27: "Daniel",
28: "Hosea",
29: "Joel",
30: "Amos",
31: "Obadiah",
32: "Jonah",
33: "Micah",
34: "Nahum",
35: "Habakkuk",
36: "Zephaniah",
37: "Haggai",
38: "Zechariah",
39: "Malachi",
40: "Matthew",
41: "Mark",
42: "Luke",
43: "John",
44: "Acts",
45: "Romans",
46: "1 Corinthians",
47: "2 Corinthians",
48: "Galatians",
49: "Ephesians",
50: "Philippians",
51: "Colossians",
52: "1 Thessalonians",
53: "2 Thessalonians",
54: "1 Timothy",
55: "2 Timothy",
56: "Titus",
57: "Philemon",
58: "Hebrews",
59: "James",
60: "1 Peter",
61: "2 Peter",
62: "1 John",
63: "2 John",
64: "3 John",
65: "Jude",
66: "Revelation"
}
Book_names_ua={
1: "1 Мойсея",
2: "2 Мойсея",
3: "3 Мойсея",
4: "4 Мойсея",
5: "5 Мойсея",
6: "Иозея",
7: "Суддїв",
8: "Рути",
9: "1 Самуїлова",
10: "2 Самуїлова",
11: "1 Царів",
12: "2 Царів",
13: "1 Паралипоменон",
14: "2 Паралипоменон",
15: "Ездри",
16: "Неємії",
17: "Естери",
18: "Йова",
19: "Псалтирь",
20: "Приповісток",
21: "Екклезіаста",
22: "Пісень",
23: "Ісаїї",
24: "Еремії",
25: "Плач",
26: "Езекиїла",
27: "Даниїла",
28: "Осії",
29: "Йоіла",
30: "Амоса",
31: "Авдія",
32: "Йони",
33: "Михея",
34: "Наума",
35: "Аввакума",
36: "Софонії",
37: "Аггея",
38: "Захарії",
39: "Малахія",
40: "Маттея",
41: "Марка",
42: "Луки",
43: "Йоана",
44: "Дїяння",
45: "Римлян",
46: "1 Коринтян",
47: "2 Коринтян",
48: "Галат",
49: "Єфесян",
50: "Филипян",
51: "Колосян",
52: "1 Солунян",
53: "2 Солунян",
54: "1 Тимотея",
55: "2 Тимотея",
56: "Тита",
57: "Филимона",
58: "Жидів",
59: "Якова",
60: "1 Петра",
61: "2 Петра",
62: "1 Йоана",
63: "2 Йоана",
64: "3 Йоана",
65: "Юди",
66: "Одкриттє"
}
chapter_counts={
1: 50,
2: 40,
3: 27,
4: 36,
5: 34,
6: 24,
7: 21,
8: 4,
9: 31,
10: 24,
11: 22,
12: 25,
13: 29,
14: 36,
15: 10,
16: 13,
17: 10,
18: 42,
19: 150,
20: 31,
21: 12,
22: 8,
23: 66,
24: 52,
25: 5,
26: 48,
27: 12,
28: 14,
29: 3,
30: 9,
31: 1,
32: 4,
33: 7,
34: 3,
35: 3,
36: 3,
37: 2,
38: 14,
39: 4,
40: 28,
41: 16,
42: 24,
43: 21,
44: 28,
45: 16,
46: 16,
47: 13,
48: 6,
49: 6,
50: 4,
51: 4,
52: 5,
53: 3,
54: 6,
55: 4,
56: 3,
57: 1,
58: 13,
59: 5,
60: 5,
61: 3,
62: 5,
63: 1,
64: 1,
65: 1,
66: 22
}