# Doomsday Rule

Figure out day of the week for any given date.

1. Identify the **century doomsday**.

    This just needs to be memorized. Repeats every 400 years.

    #### Century Doomsday
      |  | | | |
      | -----| -----| -----| -----
      | 1500 | 1600 | 1700 | 1800
      | 1900 | 2000 | 2100 | 2200
      | 2300 | 2400 | 2500 | 2600
      | **Wed**  | **Tues** | **Sun** | **Fri**

2. Calculate the **year doomsday**.
  - a. Take the century doomsday.
  - b. Divide the year's last two digits by **12** and get the quotient.
  - c. Get the remainder of b.
  - d. Divide the remainder by **4** and get the quotient.
  - e. Sum up a+b+c+d.
  - f. Modulo e by 7 and get the remainder.

    For example, 2023:

    | | |
    | --- | --- |
    | a) Century doomsday     | 2
    | b) 23 / 12              | 1
    | c) 23 % 12              | 11
    | d) 11 / 4               | 2
    | e)      | 16
    | f) 16 % 7               | 2 (**2023's doomsday**)

3. Identify the **doomsday for each month**.

    #### Monthly Doomsday
    |  | | | |    |  | | | | | ||
    | -----| -----| -----| -----  | -----| -----| -----| -----  | -----| -----| -----| -----|
    | 1/3, 1/4 (L) | 2/28, 2/29 (L) | 3/14 | 4/4 | 5/9 | 6/6 | 7/11 | 8/8 | 9/5 | 10/10 | 11/7 | 12/12
    - Jan 3 for normal year, Jan 4 for leap year
    - Feb 28 for normal year, Feb 29 for leap year
    - March = pi day
    - even months from April - December, same day as month
    - work 9 to 5 at 7/11 + vice versa

    #### Leap years (every 4 years)
    - A year is a leap year if it is divisible by 4 but not by 100, unless it's divisible by 400.

4. Find the target date counting from the closest month doomsday.
