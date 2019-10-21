package Email;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStream;
import java.util.*;
import javax.mail.*;
import javax.mail.internet.*;
//import javax.activation.*;

public class sendEmail {
	public static void main(String [] args) throws IOException{
		Properties p = new Properties();
		InputStream is = new FileInputStream("Config.properties");
		p.load(is);
	      String to = p.getProperty("myEmail");
	      System.out.println(to);
//	      String from = "sonoojaiswal1987@gmail.com";
//	      String host = "localhost";//or IP address
//
//	     //Get the session object
//	      Properties properties = System.getProperties();
//	      properties.setProperty("mail.smtp.host", host);
//	      Session session = Session.getDefaultInstance(properties);
//
//	     //compose the message
//	      try{
//	         MimeMessage message = new MimeMessage(session);
//	         message.setFrom(new InternetAddress(from));
//	         message.addRecipient(Message.RecipientType.TO,new InternetAddress(to));
//	         message.setSubject("Ping");
//	         message.setText("Hello, this is example of sending email  ");
//
//	         // Send message
//	         Transport.send(message);
//	         System.out.println("message sent successfully....");
//
//	      }catch (MessagingException mex) {mex.printStackTrace();}
	   }
}

