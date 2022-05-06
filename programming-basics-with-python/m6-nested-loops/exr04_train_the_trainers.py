num_jury = int(input())
presentation_title = input()

average_score = 0
total_score = 0
counter = 0

while presentation_title != 'Finish':
    score_presentation = 0
    for each_person_in_jury in range(1, num_jury + 1):
        score = float(input())
        score_presentation += score

    average_score = score_presentation / num_jury
    print(f'{presentation_title} - {average_score:.2f}.')

    counter += 1
    total_score += average_score
    presentation_title = input()

final_assessment = total_score / counter
print(f'Student\'s final assessment is {final_assessment:.2f}.')
