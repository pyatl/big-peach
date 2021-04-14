This file serves as a way to track upcoming changes and log work in progress.
It is not the ultimate source of truth when it comes to features.

04/21/2020 - Added view to allow memebrs to join PyATl directly.
             Need to add a way to email all members when an event is created.
                Add the event invite as an attachment
             Need to add a way to alert all members when the event day arrived.


04/13/2020 - Changes listed below for visual updates abd redesign

landing page:

  - pass latest events as context
	- pass latest blog posts as context
	- handle form to become member
	
Blog page:

  - add featured post functionality * DONE
		- only one post can be featured * DONE
	- update post object to handle featured option * DONE

Post detail:

	- remove tags, keep categories * DONE
	- make posts searchable by author


Simplify the blog models * DONE



- Remove PostCategory model after release
- Create migration without PostCategory
- Release