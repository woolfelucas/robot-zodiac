import json

with open("./general-types.json", "r") as file:
    general_type_json = json.load(file)

def classify(input):
    robot_number = input[0]
    amp_attempts = input[1] + input[2]
    if amp_attempts != 0:
        amp_accuracy = input[1] / amp_attempts
    else:
        amp_accuracy = 0

    speaker_attempts = input[3] + input[4]
    if speaker_attempts != 0:
        speaker_accuracy = input[3] / speaker_attempts
    else:
        speaker_accuracy = 0

    shuttle_attempts = input[5]

    total_note_movement = amp_attempts + speaker_attempts + shuttle_attempts

    if total_note_movement != 0:
        amp_percentage = amp_attempts / total_note_movement
        speaker_percentage = speaker_attempts / total_note_movement
        shuttle_percentage = shuttle_attempts / total_note_movement
    else:
        return str(robot_number) + "," + "e_nnn"
    # yandev time, yippee !!! (i hate my life)

    if (general_type_json["generalist-true"]["amp-min"] < amp_percentage < general_type_json["generalist-true"][
        "amp-max"]) and (general_type_json["generalist-true"]["speaker-min"] < speaker_percentage <
                         general_type_json["generalist-true"]["speaker-max"]) and (
            general_type_json["generalist-true"]["shuttle-min"] < shuttle_percentage <
            general_type_json["generalist-true"]["shuttle-max"]):
        robot_type = "generalist-true"
    elif (general_type_json["generalist-attacker"]["amp-min"] < amp_percentage <
          general_type_json["generalist-attacker"]["amp-max"]) and (
            general_type_json["generalist-attacker"]["speaker-min"] < speaker_percentage <
            general_type_json["generalist-attacker"]["speaker-max"]):
        robot_type = "generalist-attacker"
    elif (general_type_json["amplifier"]["amp-min"] < amp_percentage):
        robot_type = "amplifier"
    elif (general_type_json["shooter"]["speaker-min"] < speaker_percentage):
        robot_type = "speaker"
    elif (general_type_json["trucker"]["shuttle-min"] < shuttle_percentage):
        robot_type = "trucker"
    else:
        robot_type = "undifferentiated"

    # that was disgusting

    return str(robot_number) + "," + robot_type + "," + str(total_note_movement)
