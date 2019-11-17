// package Menu;

import java.time.LocalDate;

public class Link {
	LocalDate currentDate = LocalDate.now();
	public int[] date = new int[3];
	public String link;

	
	public int[] getDate() {
		date[0] = currentDate.getYear();
		date[1] = currentDate.getMonthValue();
		date[2] = currentDate.getDayOfMonth();
		return date;
	}
	
	
	public String getLink() {
		getDate();
		link = String.format(
				"https://www.dickinson.edu/site/custom_scripts/dc_dining_menus_index.php?yr=%s&mo=%s&da=%s",
				Integer.toString(date[0]).substring(2, 4),
				Integer.toString(date[1]),
				Integer.toString(date[2]));
		return link;
	}
}
