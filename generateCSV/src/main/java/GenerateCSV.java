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
	    File[] files = new File("/Users/Sean/Documents/workspace/TwitterTrendDetection/json/").listFiles();
	    try {
				showFiles(files);
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		
	}
	
	public static void showFiles(File[] files) throws IOException {
	    for (File file : files) {
	        if (file.isDirectory()) {
	            System.out.println("Directory: " + file.getName());
	            showFiles(file.listFiles()); // Calls same method again.
	        } else {
	            Scanner in;
	            FileWriter fileWriter = null;
	            BufferedWriter out = null;
							try {
								in = new Scanner(file);
								System.out.println(file.getName());
								
								
								//initialize FileWriter object
								fileWriter = new FileWriter("../simplified_json/" + file.getName());
								
								//initialize CSVPrinter object 
								
								out = new BufferedWriter(fileWriter);
								while (in.hasNextLine()) {
									String json_str = in.nextLine();
									if (json_str.length() < 2) continue;
									Twitter[] twitterList = gson.fromJson(json_str, Twitter[].class);
									for (Twitter t: twitterList) {
										TwitterSimplified nt = new TwitterSimplified(t);
										out.write(gson.toJson(nt) + "\n");
									}
								}
								
								
							} catch (FileNotFoundException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							} catch (IOException e) {
								// TODO Auto-generated catch block
								e.printStackTrace();
							} finally {
								fileWriter.flush();
								out.close();
								fileWriter.close();
								
							}
	        }
	    }
	}
}
