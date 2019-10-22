package Email;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.ArrayList;
import java.util.Properties;
import java.util.Scanner;

import javax.mail.*;
import javax.mail.internet.InternetAddress;
import javax.mail.internet.MimeMessage;

import Menu.DiningMenu;
import Menu.GrabbingMenu;
import Menu.Link;
import Menu.OtherMenu;

import java.util.Properties;

/**
 * @author Crunchify.com
 * 
 */
 
public class testing {
//	static ArrayList<String> emailList = new ArrayList<>();
	private static String br = "";
	private static String[] t;
	static Properties prop = new Properties();
	private static String mes;
	
	public static void getEmailList() throws FileNotFoundException {
		File file = new File(prop.getProperty("txtLocation")); 
	      Scanner sc = new Scanner(file);
	      sc.useDelimiter("\\Z"); 
	      br = br + sc.next();
	      br = br.replaceAll("\\s+",",");
	      t = br.split(",");
	      System.out.println(br);
	}
	
	
	public static String getEmailFormat() {
		DiningMenu hall = new DiningMenu();
		OtherMenu union = new OtherMenu(GrabbingMenu.UNION);
		OtherMenu kove = new OtherMenu(GrabbingMenu.KOVE);
		
		mes = "Hello, I am Boo Sung Kim's Dickinson Menu Bot V2.0.0.\n\n"
				+ hall.formatMenu() + union.formatMenu() + kove.formatMenu()
				+ "Have a nice day!\n"
				+ "Project GitHub link: https://github.com/boosungkim/Dickinson_Menu_Bot";
		return mes;
	}
	
	
	public static void sendMail() throws FileNotFoundException {
		getEmailList();
		String fileName = "Config.properties";
		Link date = new Link();
		InputStream is = null;
		try {
		    is = new FileInputStream(fileName);
		} catch (FileNotFoundException ex) {
		}
		try {
		    prop.load(is);
		} catch (IOException ex) {
		}
		String userEmail = prop.getProperty("myEmail");
		String userPass = prop.getProperty("myPassword");
		
		prop.put("mail.smtp.host", "127.0.0.1");
        prop.put("mail.smtp.port", prop.getProperty("smtpCode"));
        prop.put("mail.smtp.auth", "true");
        prop.put("mail.smtp.starttls.enable", "true");

        
        Session session = Session.getInstance(prop,
                new javax.mail.Authenticator() {
                    protected PasswordAuthentication getPasswordAuthentication() {
                        return new PasswordAuthentication(userEmail, userPass);
                    }
                });
        //Send Email
        try {
            Message message = new MimeMessage(session);
            message.setFrom(new InternetAddress("from@gmail.com"));
            message.setRecipients(
                    Message.RecipientType.TO,
                    InternetAddress.parse("kimbo@dickinson.edu")
            );
            for(int i = 0; i < t.length; i++) {
            	message.addRecipients(Message.RecipientType.CC, InternetAddress.parse(t[i]));
            }
            message.setSubject(date.getDate()[1]+ "/" + date.getDate()[2] + "/" + date.getDate()[0]
            		+ "'s Dickinson Menu");
            message.setText(getEmailFormat());

            Transport.send(message);

            System.out.println("Done");

        } catch (MessagingException e) {
            e.printStackTrace();
        }
	}

    public static void main(String[] args) throws FileNotFoundException {
    	System.out.println(getEmailFormat());
    }

}