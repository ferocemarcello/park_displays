export function getScoreOnBody(score, gender, age, weight, height, avgWeekKm) {
  if (gender === 'F') {
    score -= 10;
  }

  if (age <= 14) {
    score -= 5;
  } else if (15 <= age && age <= 18) {
    score -= 20;
  } else if (19 <= age && age <= 23) {
    score -= 5;
  } else if (24 <= age && age <= 33) {
    // PERFECT AGE
  } else if (34 <= age && age <= 42) {
    score -= 10;
  } else if (43 <= age && age <= 55) {
    score -= 20;
  } else if (56 <= age && age <= 67) {
    score -= 25;
  } else if (68 <= age && age <= 75) {
    score -= 30;
  } else {
    score -= 35;
  }

  const bmi = weight / Math.pow(height, 2);

  if (bmi < 16) {
    score -= 10;
  } else if (16 <= bmi && bmi < 18.5) {
    score -= 5;
  } else if (18.5 <= bmi && bmi < 25) {
    // PERFECT BMI
  } else if (25 <= bmi && bmi < 30) {
    score -= 5;
  } else if (30 <= bmi && bmi < 35) {
    score -= 10;
  } else {
    score -= 15;
  }

  if (avgWeekKm && avgWeekKm < 30) {
    score -= 10;
  } else if (avgWeekKm && 30 <= avgWeekKm && avgWeekKm < 60) {
    score -= 5;
  }

  return score;
}

export function getPathScore(athleteScore, path) {
  let weightPerKm =
}