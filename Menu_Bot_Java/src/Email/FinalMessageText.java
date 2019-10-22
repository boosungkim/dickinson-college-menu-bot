package Email;

import Menu.DiningMenu;
import Menu.GrabbingMenu;
import Menu.OtherMenu;

public class FinalMessageText {
	
	public static String getEmailFormat() {
		DiningMenu hall = new DiningMenu();
		OtherMenu union = new OtherMenu(GrabbingMenu.UNION);
		OtherMenu kove = new OtherMenu(GrabbingMenu.KOVE);
	
		String mes = "Hello, I am Boo Sung Kim's Dickinson Menu Bot V2.0.0.\n\n"
				+ hall.formatMenu() + union.formatMenu() + kove.formatMenu()
				+ "Have a nice day!\n"
				+ "Project GitHub link: https://github.com/boosungkim/Dickinson_Menu_Bot";
	return mes;
}
	public static void main(String[] args) {
		System.out.println(getEmailFormat());
	}
}
