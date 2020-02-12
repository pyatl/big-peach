Templates required:



event-detail.html
context: `event`





```
<div>
	<p>Starts: {{ event.start }} </p>
	<p>Ends: {{ event.end }} </p>
</div>

<div>
	<h3>{{ event.name|capfirst }}</h3>
	<p><a href="{% url 'event-invite' pk=event.pk %}">Add to calendar</a></p>
</div>
       

<div>
	<p>{{ event.description|safe }}</p>
</div>

<div class="col-md-8">
	<p><a href="{% url 'location' slug=event.location.slug pk=event.location.pk %}">Location: {{ event.location.name|capfirst }}</a></p>
                    
	{{ event.location.map_embed_code|safe }}
</div>



```




---

events.html
context: `events`
---

location-detail.html
context: `location`
---

locations.html
context: `locations`