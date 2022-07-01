from flask import request, Blueprint
from database import db, Map, Voted

map_voting = Blueprint('map_voting', __name__)

@map_voting.route('/vote', methods = ['POST'])
def vote():
    map = int(request.form['map'])
    up = request.form['up'] == 'true'
    ip = request.remote_addr
    
    #rowcount = db.session.query(
    #    Voted.ip,
    #    Voted.map) \
    #    .filter_by(ip=ip, map=map)
    
    #if len(rowcount.all()) > 0:
    #    return "You have already voted on this map", 403

    #db.session.query(Map.id,  Map.votes) \
    #    .filter_by(id=map) \
    #    .update({Map.votes: Map.votes + (1 if up else -1)}) 
    
    #db.session.add(Voted(ip=ip, map=map))
    
    #db.session.commit()
    
    #Changed that because it wasn't working when tested it. Feel free to remove it and revert old code if it was working
    
    rowcount = db.engine.execute("SELECT * FROM voted WHERE ip = \""+str(ip)+"\" AND map = "+str(map)+";")
    if rowcount.rowcount > 0:
        return "You have already voted on this map", 403
    
    db.engine.execute("INSERT INTO voted VALUES(\""+str(ip)+"\","+str(map)+");")
    db.engine.execute("UPDATE maps SET votes = votes "+("+" if up else "-")+" 1 WHERE id="+str(map)+";")
    return "thanks"
