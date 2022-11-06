pub fn part_1(input: &Vec<String>) -> i32 {
    let mut depth = 0;
    let mut position = 0;

    let input_lenght = input.len();


    for i in 0..input_lenght {
        let command: Vec<&str> = input[i].split(' ').collect();
        let direction = command[0];
        let distance = command[1];

        if direction == "forward" {
            position += distance.parse::<i32>().unwrap();
        }
        if direction == "up" {
            depth -= distance.parse::<i32>().unwrap();
        }
        if direction == "down" {
            depth += distance.parse::<i32>().unwrap();
        }

    }

    let result = position * depth;
    return result;
}

pub fn part_2(input: &Vec<String>) -> i32 {
    let mut aim:i32 = 0;
    let mut depth:i32 = 0;
    let mut position:i32 = 0;

    let input_lenght = input.len();


    for i in 0..input_lenght {
        let command: Vec<&str> = input[i].split(' ').collect();
        let direction = command[0];
        let distance = command[1];

        if direction == "forward" {
            let step:i32 = distance.parse::<i32>().unwrap();
            position += step;
            depth = depth + aim * step;
        }
        if direction == "up" {
            aim -= distance.parse::<i32>().unwrap();
        }
        if direction == "down" {
            aim += distance.parse::<i32>().unwrap();
        }

    }

    let result: i32 = position * depth;
    return result;
}
