package Email;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.util.Properties;

/**
 * @author Crunchify.com
 * 
 */
 
public class testing {
 
	public static void main(String[] args) throws IOException {
		Properties p = new Properties();
		OutputStream os = new FileOutputStream("Config.properties");
		p.setProperty("url", "testing");
		p.store(os, null);
	}
}