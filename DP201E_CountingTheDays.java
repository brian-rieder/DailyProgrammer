package com.example.FirstJavaProject;

// Author: Brian Rieder
// Link: http://www.reddit.com/r/dailyprogrammer/comments/2vc5xq/20150209_challenge_201_easy_counting_the_days/

// Difficulty: Easy


/**
 * Sometimes you wonder. How many days I have left until.....Whatever date you are curious about. Maybe a holiday.
 * Maybe a vacation. Maybe a special event like a birthday.
 * So today let us do some calendar math. Given a date that is in the future how many days until that date from the
 * current date?
 * Input:
 * The date you want to know about in 3 integers. I leave it to you to decide if you want to do yyyy mm dd or
 * mm dd yyyy or whatever. For my examples I will be using yyyy mm dd. Your solution should have 1 comment saying what
 * format you are using for people reading your code. (Note you will need to convert your inputs to your format from
 * mine if not using yyyy mm dd)
 *
 * Output:
 * The number of days until that date from today's date (the time you run the program)
 * Example Input: 2015 2 14
 * Example Output: 5 days from 2015 2 9 to 2015 2 14
 *
 * Challenge Inputs:
 * 2015 7 4
 * 2015 10 31
 * 2015 12 24
 * 2016 1 1
 * 2016 2 9
 * 2020 1 1
 * 2020 2 9
 * 2020 3 1
 * 3015 2 9
 */

import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Date;
import java.util.Scanner;


class MyDate {
    public int month;
    public int day;
    public int year;

    public MyDate(String user_input) {
        String[] split = user_input.split("/");
        if(split.length != 3) {
            System.out.print("Invalid input\n");
            System.exit(0);
        }
        month = Integer.parseInt(split[0]);
        day = Integer.parseInt(split[1]);
        year = Integer.parseInt(split[2]);
    }

    public MyDate getCurrentDate() {
        DateFormat dateFormat = new SimpleDateFormat("MM/dd/yyyy");
        Calendar cal = Calendar.getInstance();
        Date date = new Date();
        String comp_input = dateFormat.format(date);
        MyDate curr_date = new MyDate(comp_input);
        return curr_date;
    }

    public void validateDateAgainst(MyDate today_date) {
        if (year < today_date.year || (year == today_date.year && month < today_date.month)
                || (year == today_date.year && month == today_date.month && day < today_date.day)) {
            System.out.print("Date must be AFTER today's date.");
            System.exit(0);
        }

        switch(month) {
            case 1:
                if(day > 31 || day < 1) {
                    System.out.print("January has 31 days.");
                    System.exit(0);
                }
                break;
            case 2:
                if(year % 4 == 0 && !(year % 100 == 0 && year % 400 != 0) && (day > 29 || day < 1)) {
                    System.out.print("February has 29 days that year.");
                    System.exit(0);
                }
                else if (!(year % 4 == 0 && !(year % 100 == 0 && year % 400 != 0)) && day > 28 || day < 1) {
                    System.out.print("February has 28 days that year.");
                    System.exit(0);
                }
                break;
            case 3:
                if(day > 31 || day < 1) {
                    System.out.print("March has 31 days.");
                    System.exit(0);
                }
                break;
            case 4:
                if(day > 30 || day < 1) {
                    System.out.print("April has 30 days.");
                    System.exit(0);
                }
                break;
            case 5:
                if(day > 31 || day < 1) {
                    System.out.print("May has 31 days.");
                    System.exit(0);
                }
                break;
            case 6:
                if(day > 30 || day < 1) {
                    System.out.print("June has 30 days.");
                    System.exit(0);
                }
                break;
            case 7:
                if(day > 31 || day < 1) {
                    System.out.print("July has 31 days.");
                    System.exit(0);
                }
                break;
            case 8:
                if(day > 31 || day < 1) {
                    System.out.print("August has 31 days.");
                    System.exit(0);
                }
                break;
            case 9:
                if(day > 30 || day < 1) {
                    System.out.print("September has 30 days.");
                    System.exit(0);
                }
                break;
            case 10:
                if(day > 31 || day < 1) {
                    System.out.print("October has 31 days.");
                    System.exit(0);
                }
                break;
            case 11:
                if(day > 30 || day < 1) {
                    System.out.print("November has 30 days.");
                    System.exit(0);
                }
                break;
            case 12:
                if(day > 31 || day < 1) {
                    System.out.print("December has 31 days.");
                    System.exit(0);
                }
                break;
            default:
                System.out.print("Invalid month number.");
                System.exit(0);
        }
    }

    public int countTheDaysFrom(MyDate today) {
        int num_days = 0;
        // Skip ahead a bit to make this faster
        while(year - today.year > 4) {
            num_days += 1461; //365 + 365 + 365 + 366
            today.year += 4;
        }
        // Move by year
        while(year != today.year) {
            // If it is a leap year...
            if(today.year % 4 == 0 && !(today.year % 100 == 0 && today.year % 400 != 0)) {
                num_days += 366;
                today.year += 1;
            }
            // Otherwise it isn't...
            else {
                num_days += 365;
                today.year += 1;
            }
        }
        // Move by month...
        if(month > today.month) {
            while(month != today.month) {
                switch (month) {
                    case 1:
                        today.month += 1;
                        num_days += 31;
                        break;
                    case 2:
                        today.month += 1;
                        if(year % 4 == 0 && !(year % 100 == 0 && year % 400 != 0)) {
                            num_days += 29;
                        }
                        else {
                            num_days += 28;
                        }
                        break;
                    case 3:
                        today.month += 1;
                        num_days += 31;
                        break;
                    case 4:
                        today.month += 1;
                        num_days += 30;
                        break;
                    case 5:
                        today.month += 1;
                        num_days += 31;
                        break;
                    case 6:
                        today.month += 1;
                        num_days += 30;
                        break;
                    case 7:
                        today.month += 1;
                        num_days += 31;
                        break;
                    case 8:
                        today.month += 1;
                        num_days += 31;
                        break;
                    case 9:
                        today.month += 1;
                        num_days += 30;
                        break;
                    case 10:
                        today.month += 1;
                        num_days += 31;
                        break;
                    case 11:
                        today.month += 1;
                        num_days += 30;
                        break;
                    case 12:
                        today.month += 1;
                        num_days += 31;
                        break;
                }
            }
        }
        else {
            while (month != today.month) {
                switch (month) {
                    case 1:
                        today.month -= 1;
                        num_days -= 31;
                        break;
                    case 2:
                        today.month -= 1;
                        if(year % 4 == 0 && !(year % 100 == 0 && year % 400 != 0)) {
                            num_days -= 29;
                        }
                        else {
                            num_days -= 28;
                        }
                        break;
                    case 3:
                        today.month -= 1;
                        num_days -= 31;
                        break;
                    case 4:
                        today.month -= 1;
                        num_days -= 30;
                        break;
                    case 5:
                        today.month -= 1;
                        num_days -= 31;
                        break;
                    case 6:
                        today.month -= 1;
                        num_days -= 30;
                        break;
                    case 7:
                        today.month -= 1;
                        num_days -= 31;
                        break;
                    case 8:
                        today.month -= 1;
                        num_days -= 31;
                        break;
                    case 9:
                        today.month -= 1;
                        num_days -= 30;
                        break;
                    case 10:
                        today.month -= 1;
                        num_days -= 31;
                        break;
                    case 11:
                        today.month -= 1;
                        num_days -= 30;
                        break;
                    case 12:
                        today.month -= 1;
                        num_days -= 31;
                        break;
                }
            }
        }
        // Move by day...
        if(day > today.day) {
            while (day != today.day) {
                num_days += 1;
                today.day += 1;
            }
        }
        else {
            while(day != today.day) {
                num_days -= 1;
                today.day -= 1;
            }
        }

        return num_days;
    }

    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("How many days till what date? mm/dd/yyyy: ");
        String user_input = scan.nextLine();
        MyDate till_when = new MyDate(user_input);
        MyDate today = till_when.getCurrentDate();
        till_when.validateDateAgainst(today);
        int num_days = till_when.countTheDaysFrom(today);
        System.out.print("There are " + Integer.toString(num_days) + " days until then.");
    }
}


//year % 4 == 0 && !(year % 100 == 0 && year % 400 != 0) determine it IS a leap year
