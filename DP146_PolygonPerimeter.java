// Link to reddit: http://www.reddit.com/r/dailyprogrammer/comments/1tixzk/122313_challenge_146_easy_polygon_perimeter/

// Difficulty: Easy

//A Polygon is a geometric two-dimensional figure that has n-sides (line segments) that closes to form a loop.
// Polygons can be in many different shapes and have many different neat properties, though this challenge is about
// Regular Polygons . Our goal is to compute the permitter of an n-sided polygon that has equal-length sides
// given the circumradius . This is the distance between the center of the Polygon to any of its vertices;
// not to be confused with the apothem!

// Input Description
// Input will consist of one line on standard console input. This line will contain first an integer N, then
// a floating-point number R. They will be space-delimited. The integer N is for the number of sides of the Polygon,
// which is between 3 to 100, inclusive. R will be the circumradius, which ranges from 0.01 to 100.0, inclusive.

// Output Description
// Print the permitter of the given N-sided polygon that has a circumradius of R. Print up to three digits precision.
// Sample Inputs & Outputs
// Sample Input 1
// 5 3.7
// Sample Output 1
// 21.748
// Sample Input 2
// 100 1.0
// Sample Output 2
// 6.282

import java.util.Scanner;

class Polygon {
    private int numSides;
    private float circumradius;

    public Polygon(int givenNumSides, float givenCircumradius) {
        numSides = givenNumSides;
        circumradius = givenCircumradius;
    }

    public int getNumSides() {
        return numSides;
    }

    public void setNumSides(int newVal) {
        numSides = newVal;
    }

    public float getCircumradius() {
        return circumradius;
    }

    public void setCircumradius(int newVal) {
        circumradius = newVal;
    }

    public float findSideLength() {
        float angleApothemToCircumradius = 180F / numSides;
        return 2 * circumradius * ((float) Math.sin(Math.toRadians(angleApothemToCircumradius)));
    }

    public float findPerimeter(float sideLength) {
        return sideLength * numSides;
    }
}

public class DP146_PolygonPerimeter {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.print("Enter arguments as <number of sides> <circumradius>: ");
        String[] userInput = scan.nextLine().split(" ");
        Polygon polygon = new Polygon(Integer.parseInt(userInput[0]), Float.parseFloat(userInput[1]));
        float sideLength = polygon.findSideLength();
        float perimeter = polygon.findPerimeter(sideLength);
        System.out.printf("Perimeter: %.3f\n", perimeter);
    }
}
