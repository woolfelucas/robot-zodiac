import json
import csv


# general-types.json is unused for now because bugs
general_type_json = {
    "generalist-true":{
        "amp-min":0.25,
        "amp-max":0.40,
        "speaker-min":0.25,
        "speaker-max":0.4,
        "shuttle-min":0.25,
        "shuttle-max":0.4
    },
    "generalist-attacker":{
        "amp-min":0.35,
        "amp-max":0.65,
        "speaker-min":0.35,
        "speaker-max":0.65,
    },

    "amplifier":{
        "amp-min":0.51
    },

    "shooter":{
        "speaker-min":0.51
    },

    "trucker":{
        "shuttle-min":0.51
    }
}

def classify(input):
    robot_number = input[0]
    amp_attempts = input[1]+input[2]
    if amp_attempts != 0:
        amp_accuracy = input[1]/amp_attempts
    else:
        amp_accuracy = 0
    
    speaker_attempts = input[3]+input[4]
    if speaker_attempts != 0:
        speaker_accuracy = input[3]/speaker_attempts
    else:
        speaker_accuracy = 0

    shuttle_attempts = input[5]

    total_note_movement = amp_attempts+speaker_attempts+shuttle_attempts

    if total_note_movement != 0:
        amp_percentage = amp_attempts/total_note_movement
        speaker_percentage = speaker_attempts/total_note_movement
        shuttle_percentage = shuttle_attempts/total_note_movement
    else:
        return [robot_number, "Error: No Note Movement"]
    #yandev time, yippee !!! (i hate my life)

    if (general_type_json["generalist-true"]["amp-min"] < amp_percentage < general_type_json["generalist-true"]["amp-max"]) & (general_type_json["generalist-true"]["speaker-min"] < speaker_percentage < general_type_json["generalist-true"]["speaker-max"]) & (general_type_json["generalist-true"]["shuttle-min"] < shuttle_percentage < general_type_json["generalist-true"]["shuttle-max"]):
        robot_type = "generalist-true"
    elif (general_type_json["generalist-attacker"]["amp-min"] < amp_percentage < general_type_json["generalist-attacker"]["amp-max"]) & (general_type_json["generalist-attacker"]["speaker-min"] < speaker_percentage < general_type_json["generalist-attacker"]["speaker-max"]):
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

    return [robot_number, robot_type, total_note_movement]


# actual code starts here

output_file = open("./output.txt", "w")

with open("./data.csv", newline='') as csvfile:
    dataCSV = csv.reader(csvfile)
    for lines in dataCSV:
        if lines[0].find("#") == -1:
            int_lines = [int(entry) for entry in lines]
            output_file.write(str(classify(int_lines))+",\n")







#file = open("general-types.json")

#general_types = json.load(file)

#for i in general_types["generalist-true"]:
#    print(i)

#json.close()

