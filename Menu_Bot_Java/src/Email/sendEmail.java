package Email;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;
import java.io.File; 
import java.io.FileNotFoundException; 
import java.util.Scanner;
import java.util.logging.Level;
import java.util.logging.Logger; 



public class sendEmail {
//	static ArrayList<String> emailList = new ArrayList<>();
	static String[] t;
	static Properties p = new Properties();
	
	public void getEmailList() throws FileNotFoundException {
		File file = new File(p.getProperty("txtLocation")); 
	      Scanner sc = new Scanner(file);
	      sc.useDelimiter("\\Z"); 
//	      t = emailList.add(sc.next());
	}
	
	
	public static void sendMail(String test) throws IOException, MessagingException {
		Properties properties = System.getProperties();
		InputStream is = new FileInputStream("Config.properties");
		p.load(is);
		p.put("mail.smtp.auth", "true");
		p.put("mail.smtp.starttls.enable", "true");
		p.put("mail.smtp.host", "smtp.gmail.com");
		p.put("mail.smtp.port", "587");
//		p.put("mail.smtp.ssl.trust", "smtp.gmail.com");
//		properties.put("mail.smtp.ssl.trust", "STARTTLS");
		
	      // Sender's email ID needs to be mentioned
//	      String from = properties.getProperty("dickinson_menu_bot@protonmail.com");
//	      String pass = properties.getProperty("tCj1JH7A-NHD7TDY8PqBEA");

	      // Assuming you are sending email from localhost
//	      String host = p.getProperty("hostName");

	      Session session = Session.getInstance(properties, new Authenticator(){
	    	  @Override
	    	  protected PasswordAuthentication getPasswordAuthentication() {
	    		  return new PasswordAuthentication("versatileboo@gmail.com", "iagtbtvbaptw275");
	    	  }
	      });
//	      session.getProperties().put("mail.smtp.starttls.enable", "true");
	      Message message = prepareMessage(session, "versatileboo@gmail.com", test);
	      
	      Transport.send(message);
	      
	}
	
	
	public static Message prepareMessage(Session session, String myEmail, String rec) {
		try {
			MimeMessage message = new MimeMessage(session);
			message.setFrom(new InternetAddress(myEmail));
			message.setRecipients(Message.RecipientType.TO, rec);
//			for(String r : emailList) {
//	        	 message.addRecipient(Message.RecipientType.TO, new InternetAddress(r));
//	         }
			message.setSubject("This is the Subject Line!");
			message.setText("This is actual message");
			return message;
			
		} catch (Exception e) {
			Logger.getLogger(sendEmail.class.getName()).log(Level.SEVERE, null, e);;
		}
		return null;
		
	}
	
	public static void main(String[] args) throws IOException, FileNotFoundException, MessagingException{
		sendEmail.sendMail("kimbo@dickinson.edu");
//	      }
	   }
}

