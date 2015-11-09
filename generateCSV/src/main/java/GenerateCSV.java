import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

import com.google.gson.Gson;


public class GenerateCSV {
	private static Gson gson = new Gson();
	public static void main(String... args) {
//	    File[] files = new File("/Users/Sean/Documents/workspace/TwitterTrendDetection/json/").listFiles();
//	    try {
//				showFiles(files);
//			} catch (IOException e) {
//				// TODO Auto-generated catch block
//				e.printStackTrace();
//			}
		int [] cells = {1,1,1,0,1,1,1,1};
		int [] results = cellCompete(cells, 2);
		for (int ele : results) {
			System.out.println(ele);
		}
		
	}
	
	public static int[] cellCompete(int[] cells, int days) {
		if (cells == null || days <= 0)	return cells;
		int length = cells.length;
		int[] newCells = new int[length + 2];
		newCells[0] = newCells[length+1] = 0;
		int prev = newCells[0];
		for (int i = 1; i <= length; i++)
			newCells[i] = cells[i-1];
		for (int i = 0; i < days; i++) {
			prev = 0;
			for (int j = 1; j <= length; j++) {
				int temp = newCells[j];
				newCells[j] = prev ^ newCells[j+1];
				prev = temp;
			}
		}
		return Arrays.copyOfRange(newCells, 0, length+2);
	}
//	public static void showFiles(File[] files) throws IOException {
//	    for (File file : files) {
//	        if (file.isDirectory()) {
//	            System.out.println("Directory: " + file.getName());
//	            showFiles(file.listFiles()); // Calls same method again.
//	        } else {
//	            Scanner in;
//	            FileWriter fileWriter = null;
//	            BufferedWriter out = null;
//							try {
//								in = new Scanner(file);
//								System.out.println(file.getName());
//								
//								
//								//initialize FileWriter object
//								fileWriter = new FileWriter(file.getName());
//								
//								//initialize CSVPrinter object 
//								
//								out = new BufferedWriter(fileWriter);
//								while (in.hasNextLine()) {
//									String json_str = in.nextLine();
//									if (json_str.length() < 2) continue;
//									Twitter[] twitterList = gson.fromJson(json_str, Twitter[].class);
//									for (Twitter t: twitterList) {
//										TwitterSimplified nt = new TwitterSimplified(t);
//										out.write(gson.toJson(nt) + "\n");
//									}
//								}
//								
//								
//							} catch (FileNotFoundException e) {
//								// TODO Auto-generated catch block
//								e.printStackTrace();
//							} catch (IOException e) {
//								// TODO Auto-generated catch block
//								e.printStackTrace();
//							} finally {
//								fileWriter.flush();
//								out.close();
//								fileWriter.close();
//								
//							}
//	        }
//	    }
//	}
}
