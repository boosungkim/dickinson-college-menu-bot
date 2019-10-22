package Menu;

public class OtherMenu extends DiningMenu{
	public int wMeal;
	public OtherMenu(int w) {
		super();
		wMeal = w;
		}
	
	
	public String formatMenu() {
		String diningEmail = "";
		if(wMeal == GrabbingMenu.UNION) {
			diningEmail = "Today's Union Station Menu is:\n";
		}else if(wMeal == GrabbingMenu.KOVE) {
			diningEmail = "Today's Kove Menu is:\n";
		}
		diningEmail =	diningEmail
						+ "---Lunch---\n"
						+ formatSection("", wMeal, GrabbingMenu.FIRST)
						+ "---Dinner---\n"
						+ formatSection("", wMeal, GrabbingMenu.SECOND)
						+ "\n\n";
		return diningEmail;
	}
}
