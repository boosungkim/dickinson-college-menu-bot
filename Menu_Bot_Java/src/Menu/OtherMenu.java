package Menu;

public class OtherMenu extends DiningMenu{
	public OtherMenu() {
		super();
//		System.out.println(formatMenu());
	}
	
	
	public String formatMenu() {
		String diningEmail = "Today's Dining Hall Menu is:\n"
				+ "---Lunch---\n"
				+ formatSection("", GrabbingMenu.DINING, GrabbingMenu.FIRST)
				+ "---Dinner---\n"
				+ formatSection("", GrabbingMenu.DINING, GrabbingMenu.SECOND)
				+ "\n\n";
		return diningEmail;
	}
}
